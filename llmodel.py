
from transformers import pipeline
from recommendfunctionality import get_suggestion
from weatherfunctionality import get_weather


pipe = pipeline("text2text-generation", model="google/flan-t5-base")
# Agent logic — simulate reasoning and reflection
def agent_response(user_input):
    # Direct weather detection via simple pattern
    if "weather in" in user_input.lower():
        try:
            # Basic city name extraction
            ####user_input.lower() - Converts the input text to lowercase
            # split("weather in")[1] - Splits the text at "weather in" and takes everything after it
            # strip() - Removes leading and trailing whitespace
            # rstrip('?') - Removes question mark from the end if present
            # capitalize() - Capitalizes the first letter of the city name
            city = user_input.lower().split("weather in")[1].strip().rstrip('?').capitalize()
            city, desc, temp = get_weather(city)

            return f"The weather in {city} is {desc} with a temperature of {temp}°C.\n\n{get_suggestion(desc, temp)}"
        except Exception as e:
            return f"I couldn't get the weather information for that location. Error: {str(e)}"
    
    # Fall back to model if user input isn't explicit
    
    prompt = (
        f"You are an assistant, respond politely and help me with the weather{user_input}"
    )

    result = pipe(prompt)
    # result = qa_pipeline(prompt)[0]["generated_text"]
    print(result[0]['generated_text'])
    if "WEATHER" in result[0]['generated_text'].upper():
        try:
            # city = result[0]['generated_text'].split(":")[1].strip().capitalize()
            # city, desc, temp = get_weather(city)
            city = user_input.lower().split("weather")[1].strip().rstrip('?').capitalize()
            city, desc, temp = get_weather(city)

            return f"{result[0]['generated_text']}.\n\n The weather in {city} is {desc} with a temperature of {temp}°C.\n\n{get_suggestion(desc, temp)}"
        except Exception as e:
            return f"I couldn't get the weather information for that location. Error: {str(e)}"
    else:
        return result[0]['generated_text'] 