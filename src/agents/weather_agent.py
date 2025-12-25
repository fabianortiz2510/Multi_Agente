import re
from src.tools.weather_service import get_weather


class WeatherAgent:
    def run(self, user_input: str) -> str:
        city = self.extract_city(user_input)
        return get_weather(city)

    def extract_city(self, text: str) -> str:
        text_clean = text.lower().strip()

        # 1️⃣ Casos con frase
        patterns = [
            r"clima en ([a-záéíóúñ\s]+)",
            r"tiempo en ([a-záéíóúñ\s]+)",
            r"temperatura en ([a-záéíóúñ\s]+)"
        ]

        for pattern in patterns:
            match = re.search(pattern, text_clean)
            if match:
                return match.group(1).strip().title()

        # 2️⃣ Caso: solo ciudad (Bogotá, Medellín, Cali, etc.)
        if re.fullmatch(r"[a-záéíóúñ\s]+", text_clean):
            return text_clean.title()

        raise ValueError("No se pudo identificar la ciudad en la pregunta")
