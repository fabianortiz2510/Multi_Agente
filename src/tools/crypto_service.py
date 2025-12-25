import requests

def get_crypto_price(coin: str) -> str:
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        f"?ids={coin}&vs_currencies=usd"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    if coin not in data:
        raise ValueError("Criptomoneda no encontrada")

    price = data[coin]["usd"]
    return f"El precio actual de {coin} es ${price} USD"
