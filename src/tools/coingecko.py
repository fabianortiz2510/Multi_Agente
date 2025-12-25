import requests

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"


def get_crypto_price(coin: str, currency: str = "usd") -> float:
    params = {
        "ids": coin,
        "vs_currencies": currency,
    }
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()[coin][currency]
