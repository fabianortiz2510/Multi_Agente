from langgraph.graph import StateGraph
from typing import TypedDict
from src.llm.client import llm
from src.agents.weather_agent import WeatherAgent
from src.agents.crypto_agent import CryptoAgent
from src.agents.rag_agent import RagAgent
from src.agents.geocoding_agent import GeocodingAgent


# 🔹 Estado compartido
class AgentState(TypedDict):
    input: str
    output: str


weather_agent = WeatherAgent()
crypto_agent = CryptoAgent()
rag_agent = RagAgent()
geo_agent = GeocodingAgent()


def route(state: AgentState):
    text = state["input"].lower()

    # 🔹 WEATHER
    if any(k in text for k in ["clima", "temperatura", "pronóstico", "lluvia"]):
        return "weather"

    # 🔹 CRYPTO
    if any(k in text for k in ["bitcoin", "ethereum", "precio", "crypto", "criptomoneda"]):
        return "crypto"

    # 🔹 GEOCODING (SOLO CUANDO PIDEN UBICACIÓN)
    if any(k in text for k in [
        "dónde queda",
        "donde queda",
        "ubicación exacta",
        "dirección de",
        "coordenadas",
        "latitud",
        "longitud"
    ]):
        return "geo"

    # 🔹 RAG POR DEFECTO
    return "rag"


# 🔹 NODOS
def geo_node(state: AgentState):
    state["output"] = geo_agent.run(state["input"])
    return state


def weather_node(state: AgentState):
    state["output"] = weather_agent.run(state["input"])
    return state


def crypto_node(state: AgentState):
    state["output"] = crypto_agent.run(state["input"])
    return state


def rag_node(state: AgentState):
    state["output"] = rag_agent.run(state["input"])
    return state


# 🔹 GRAPH
graph = StateGraph(AgentState)

graph.add_node("weather", weather_node)
graph.add_node("crypto", crypto_node)
graph.add_node("geo", geo_node)
graph.add_node("rag", rag_node)

graph.set_conditional_entry_point(
    route,
    {
        "weather": "weather",
        "crypto": "crypto",
        "geo": "geo",
        "rag": "rag"
    }
)

graph.set_finish_point("weather")
graph.set_finish_point("crypto")
graph.set_finish_point("geo")
graph.set_finish_point("rag")

assistant_graph = graph.compile()
