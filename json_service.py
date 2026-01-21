import json
import os

def data_done(new_data):
  filename = "weather_history.json"

  if os.path.exists(filename):
    with open(filename, "r") as file:
      try:
        data = json.load(file)
      except json.JSONDecodeError:
        data = []
  else:
    data = [] 


  data.append(new_data)       

  with open(filename, "w") as file:
    json.dump(data, file, indent=2)
    