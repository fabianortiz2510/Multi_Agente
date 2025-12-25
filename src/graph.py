from langgraph.graph import StateGraph
from typing import TypedDict
from src.llm.client import llm
from src.agents.weather_agent import WeatherAgent
from src.agents.crypto_agent import CryptoAgent
from src.agents.rag_agent import RagAgent


# 🔹 Estado compartido
class AgentState(TypedDict):
    input: str
    output: str


weather_agent = WeatherAgent()
crypto_agent = CryptoAgent()
rag_agent = RagAgent()


# 🔹 NODOS
def route(state: AgentState):
    prompt = f"""
Decide a qué agente enviar la pregunta:

- weather → clima
- crypto → precios de criptomonedas
- rag → preguntas sobre documentos locales

Pregunta: {state['input']}

Responde solo con: weather, crypto o rag
"""
    decision = llm.invoke(prompt).content.strip()
    return decision


def weather_node(state: AgentState):
    state["output"] = weather_agent.run(state["input"])
    return state


def crypto_node(state: AgentState):
    state["output"] = crypto_agent.run(state["input"])
    return state


def rag_node(state: AgentState):
    state["output"] = rag_agent.run(state["input"])
    return state

graph = StateGraph(AgentState)

graph.add_node("weather", weather_node)
graph.add_node("crypto", crypto_node)
graph.add_node("rag", rag_node)

graph.set_conditional_entry_point(
    route,
    {
        "weather": "weather",
        "crypto": "crypto",
        "rag": "rag"
    }
)

graph.set_finish_point("weather")
graph.set_finish_point("crypto")
graph.set_finish_point("rag")

assistant_graph = graph.compile()
