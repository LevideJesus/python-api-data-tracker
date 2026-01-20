from api_service import api_request
from utils import weather_data

def menu():
  print("="*50)
  print("Welcome to the weather check")
  print("="*50)

  print("1 - Get the Weather Data")
  print("2 - Exit ")

  choice = input("Enter your choose: ")
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
       print(f"City: {clean_data["city"]}")
       print(f"Country: {clean_data["country"]}")
       print(f"Weather: {clean_data["weather"]}")
       print(f"Temp: {clean_data["temperature"]}")
  

    elif users_choice == "2":
      print("Bye...")
      break
    else:
      print("You must type just 1 or 2")
      continue

main()