import requests

BASE_URL = "https://nominatim.openstreetmap.org/search"


def get_coordinates(city: str) -> tuple[float, float]:
    params = {
        "q": city,
        "format": "json",
        "limit": 1,
    }
    headers = {"User-Agent": "multi-agent-app"}

    response = requests.get(BASE_URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()
    if not data:
        raise ValueError(f"City not found: {city}")

    return float(data[0]["lat"]), float(data[0]["lon"])
