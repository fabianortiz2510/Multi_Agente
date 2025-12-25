import re
from src.agents.weather_agent import WeatherAgent
from src.agents.crypto_agent import CryptoAgent
from src.agents.rag_agent import RagAgent


class Orchestrator:
    def __init__(self):
        self.weather_agent = WeatherAgent()
        self.crypto_agent = CryptoAgent()
        self.rag_agent = RagAgent()

    def route(self, user_input: str) -> str:
        text = user_input.lower().strip()

        # 1️⃣ Crypto
        if any(word in text for word in ["bitcoin", "btc", "ethereum", "eth"]):
            return self.crypto_agent.run(user_input)

        # 2️⃣ Weather explícito
        if any(word in text for word in ["clima", "tiempo", "temperatura"]):
            return self.weather_agent.run(user_input)

        # 3️⃣ RAG explícito (documentos)
        if any(word in text for word in ["documento", "documentos", "archivos", "según", "información"]):
            return self.rag_agent.run(user_input)

        # 4️⃣ Solo ciudad → clima
        if re.fullmatch(r"[a-záéíóúñ\s]+", text):
            return self.weather_agent.run(user_input)

        # 5️⃣ Default → RAG
        return self.rag_agent.run(user_input)
