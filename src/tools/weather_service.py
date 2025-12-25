import requests
from src.tools.geocoding import get_coordinates


def get_weather(city: str) -> str:
    lat, lon = get_coordinates(city)

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&current_weather=true"
    )

    response = requests.get(url, timeout=10)
    data = response.json()

    weather = data["current_weather"]

    return (
        f"Clima actual en {city.title()}:\n"
        f"Temperatura: {weather['temperature']}°C\n"
        f"Viento: {weather['windspeed']} km/h"
    )
