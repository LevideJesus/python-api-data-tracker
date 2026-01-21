from dotenv import load_dotenv
import os 
import requests

load_dotenv()
api_key = os.getenv("API_KEY")
base_url = "https://api.openweathermap.org/data/2.5/weather"

def api_request(name, code):
  url = f"{base_url}?q={name},{code}&appid={api_key}"
  response = requests.get(url)

  if response.status_code == 200:
    weather_data = response.json()
    return weather_data
  else:
    return None


