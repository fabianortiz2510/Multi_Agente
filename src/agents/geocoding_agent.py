import requests
import time
from src.llm.client import llm


class GeocodingAgent:
    def extract_place(self, question: str) -> str:
        """
        Usa el LLM para extraer SOLO el lugar de la pregunta
        """
        prompt = f"""
Extrae únicamente el nombre del lugar de la siguiente pregunta.
No agregues explicaciones, solo el nombre del lugar.

Pregunta:
{question}
"""
        response = llm.invoke(prompt).content.strip()
        return response


    def run(self, query: str) -> str:
        # ⏱ Rate limit obligatorio
        time.sleep(1)

        place = self.extract_place(query)

        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": place,
            "format": "json",
            "limit": 1
        }

        headers = {
            "User-Agent": "multi-agent-assistant"
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code != 200:
            return "Error consultando el servicio de geocodificación."

        data = response.json()
        if not data:
            return f"No se encontró información para: {place}"

        result = data[0]

        return (
            "📍 Lugar encontrado:\n"
            f"{result['display_name']}\n"
            f"Latitud: {result['lat']}\n"
            f"Longitud: {result['lon']}"
        )
