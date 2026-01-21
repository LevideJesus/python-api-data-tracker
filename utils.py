def weather_data(raw_data):

  weather_data = {
    "city": raw_data["name"],
    "country": raw_data["sys"]["country"],
    "weather":raw_data["weather"][0]["main"],
    "temperature": raw_data["main"]["temp"]- 273.15
  
  }

  return weather_data