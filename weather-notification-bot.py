import requests

API_KEY = "your_openweather_api_key"
CITY = "Lucknow"
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url).json()
print(response)
temp = response["main"]["temp"]
weather = response["weather"][0]["description"]
print(f"current weather in {CITY}: {temp}°C,{weather}")
