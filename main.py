from api_service import api_request

def menu():
  print("="*50)
  print("Welcome to the weather check")
  print("="*50)

  print("1 - Get the Weather Data")
  print("2 - Exit ")
  
  choice = input("Enter your choose: ")
  return choice


def main():

  while True:
    users_choice = menu()
    if users_choice == "1":
      continue
    elif users_choice == "2":
      print("Bye...")
      break
    else:
      print("You must type just 1 or 2")
      continue

main()