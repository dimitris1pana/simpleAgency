import requests
import os
from dotenv import load_dotenv

# HF pipeline for instruction-following
load_dotenv()

# External CALLS 
WEATHER_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")


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

