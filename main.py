import json
from api_service import api_request
from utils import weather_data
from json_service import data_done

def menu():
  print("="*50)
  print("Welcome to the weather check")
  print("="*50)

  print("1 - Get the Weather Data")
  print("2 - Show History")
  print("3 - Exit ")

  choice = input("Enter your choise: ")
  return choice

def get_location():
  city_name = input("Enter the city´s name that you want: ")

  country_code = input("Enter the country code (example: BR, US, GB): ")

  return city_name, country_code



def main():

  while True:
    users_choice = menu()
    if users_choice == "1":
      city_name, country_code = get_location()
      data = api_request(city_name, country_code)
      if data:
       clean_data = weather_data(data)
       print(f"City: {clean_data['city']}")
       print(f"Country: {clean_data['country']}")
       print(f"Weather: {clean_data['weather']}")
       print(f"Temp: {clean_data['temperature']}")

       data_done(clean_data)

    elif users_choice == "2":
      try:
        with open("weather_history.json", "r") as file:
          x = json.load(file)
          for items in x:
             print(f"City: {items['city']}, Country: {items['country']}, Weather: {items['weather']}, Temp: {items['temperature']:.2f}")
             print()
            

      except (FileNotFoundError, json.JSONDecodeError):
        print("No history yet. Get some weather first!")

    elif users_choice == "3":
      print("Bye...")
      break

    else:
      print("You must type just 1, 2 or 3")
      continue

main()