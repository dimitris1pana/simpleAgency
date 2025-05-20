import gradio as gr
import requests
from transformers import pipeline
import os
from dotenv import load_dotenv

# HF pipeline for instruction-following
load_dotenv()

# External CALLS 
WEATHER_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")


# Cell 2: Weather function
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad status codes
        
        data = r.json()
        if 'weather' not in data or 'main' not in data:
            return f"Error: Invalid response format for {city}"       
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
    
        # return f"The weather in {city} is {desc} with a temperature of {temp}°C."
        return city,desc,temp
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather: {str(e)}"
    except (KeyError, IndexError) as e:
        return f"Error parsing weather data: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def get_suggestion(weather_desc, temp):
    """Helper function to generate weather-appropriate suggestions"""
    suggestions = []
    
    # Temperature based suggestions
    if temp >= 20:
        suggestions.append("It's quite warm - don't forget sunscreen and stay hydrated!")
    elif temp <= 10:
        suggestions.append("It's cold - remember to dress warmly!")
        
    # Weather condition based suggestions
    if any(word in weather_desc.lower() for word in ['rain', 'shower', 'drizzle', 'thunderstorm']):
        suggestions.append("Take an umbrella with you!")
    elif any(word in weather_desc.lower() for word in ['clear', 'sunny', 'sun']):
        suggestions.append("Don't forget your sunglasses!")
    elif 'cloud' in weather_desc.lower():
        suggestions.append("It might be changeable weather - be prepared!")
        
    return " ".join(suggestions) if suggestions else ""

# Agent logic — simulate reasoning and reflection
def agent_response(user_input):
    # weather detection via simple pattern recognition
    if "weather in" in user_input.lower():
        try:
            # Basic city name extraction
            city = user_input.lower().split("weather in")[1].strip().rstrip('?').capitalize()
            city, desc, temp = get_weather(city)

            return f"The weather in {city} is {desc} with a temperature of {temp}°C.\n\n{get_suggestion(desc, temp)}"
        except Exception as e:
            return f"I couldn't get the weather information for that location. Error: {str(e)}"
    
    # Fall back to model if user input isn't explicit
    prompt = (
        f"I a weather assistant. If question does not include weather say that I am a weather assistant.\n" 
        f"{user_input}"
    )


    result = qa_pipeline(prompt)
    # result = qa_pipeline(prompt)[0]["generated_text"]
    print(result[0]['generated_text'])

    if result[0]['generated_text'].upper().startswith("WEATHER:"):
        try:
            # city = result[0]['generated_text'].split(":")[1].strip().capitalize()
            # city, desc, temp = get_weather(city)
            return result[0]['generated_text']    
        except Exception as e:
            return f"I couldn't get the weather information for that location. Error: {str(e)}"
    else:
        return result[0]['generated_text']    
    
    
    # Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🧠 Agentic Weather Assistant (Hugging Face Model)")
    user_input = gr.Textbox(label="Ask something", placeholder="e.g., What's the weather in Athens?")
    output = gr.Textbox(label="Agent's reply", lines=6)
    btn = gr.Button("Ask")

    btn.click(fn=agent_response, inputs=user_input, outputs=output)

demo.launch()