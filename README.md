
# 🌤️ Weather Tracker CLI App

A **Python command-line application** that allows you to check the weather for any city worldwide and keeps a **history of all your searches**. Built for simplicity and readability, powered by the **OpenWeatherMap API**. 

---

## ✨ Features

- 🌍 Get real-time weather data for any city  
- 🏙️ Display city, country, weather condition, and temperature  
- 📜 Maintain a **history of all previous searches** - 👀 View history in a **clean, readable format** - ✅ Simple and intuitive **CLI menu** ---

## 📖 Demo


## Welcome to the Weather Tracker

1 - Get the Weather Data
2 - Show History
3 - Exit
Enter your choice: 1

Enter the city's name that you want: São Paulo
Enter the country code (example: BR, US, GB): BR

City: São Paulo
Country: BR
Weather: Clouds
Temp: 18.2°C

==================================================

History Example:
City: São Paulo, Country: BR, Weather: Clouds, Temp: 18.2°C
City: London, Country: GB, Weather: Rain, Temp: 12.5°C

## 🚀 Installation

1. Clone the repository:

git clone [https://github.com/your-username/weather-tracker.git](https://github.com/your-username/weather-tracker.git)
cd weather-tracker

2. Set up a virtual environment:

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt


4. Configure your API Key: Create a .env file in the root directory and add your OpenWeatherMap API key:

API_KEY=your_api_key_here


5. Run the app:

python main.py

========================================================================

## 📊 Data Format:
{
  "city": "São Paulo",
  "country": "BR",
  "weather": "Clouds",
  "temperature": 18.2
}

===========================================================================
## 🛠️ Requirements
  - Python 3.x

  - requests

  - python-dotenv

