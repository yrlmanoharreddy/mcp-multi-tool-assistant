import os
import requests
from dotenv import load_dotenv
import json

load_dotenv("../.env")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")



def get_weather(city: str):
    
    if  not OPENWEATHER_API_KEY:
        print("API key loaded:", bool(OPENWEATHER_API_KEY))
        return {
            "error" : "OpenWeather API is not Configured"
        }
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        return {
            "error" : f"Weather request failed: {error}"
        }
