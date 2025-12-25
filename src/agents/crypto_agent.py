from src.tools.crypto_service import get_crypto_price

class CryptoAgent:
    def run(self, user_input: str) -> str:
        text = user_input.lower()

        if "bitcoin" in text:
            return get_crypto_price("bitcoin")
        if "ethereum" in text:
            return get_crypto_price("ethereum")

        raise ValueError("No se pudo identificar la criptomoneda")
