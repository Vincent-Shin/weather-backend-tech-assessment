import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Location not found")

    data = response.json()

    return {
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }
def get_air_quality(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    return data["list"][0]["main"]["aqi"]

def calculate_risk(temp, aqi):
    score = 0

    if temp < 0 or temp > 35:
        score += 40
    elif temp < 5 or temp > 30:
        score += 20

    if aqi and aqi >= 4:
        score += 40
    elif aqi == 3:
        score += 20

    if score >= 60:
        return "High"
    elif score >= 30:
        return "Moderate"
    else:
        return "Low"