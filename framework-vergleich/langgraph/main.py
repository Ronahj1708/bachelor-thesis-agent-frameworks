from typing import TypedDict
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)


class ReiseState(TypedDict):
    reiseziel: str
    tage: int
    budget: int
    reiseplan_text: str


def begruessung(state: ReiseState):
    print("Willkommen!")
    print(f"Reiseziel: {state['reiseziel']}")
    print(f"Tage: {state['tage']}")
    print(f"Budget: {state['budget']} €")

    return state


def reiseplan(state: ReiseState):
    print("Ich erstelle jetzt deinen Reiseplan.")

    state["reiseplan_text"] = (
        f"Reise nach {state['reiseziel']} "
        f"für {state['tage']} Tage "
        f"mit einem Budget von {state['budget']} €."
    )

    return state


def ausgabe(state: ReiseState):
    print("\nDein Reiseplan:")
    print(state["reiseplan_text"])

    return state


graph_builder = StateGraph(ReiseState)

graph_builder.add_node("begruessung", begruessung)
graph_builder.add_node("reiseplan", reiseplan)
graph_builder.add_node("ausgabe", ausgabe)

graph_builder.add_edge("begruessung", "reiseplan")
graph_builder.add_edge("reiseplan", "ausgabe")

graph_builder.set_entry_point("begruessung")
graph_builder.set_finish_point("ausgabe")

graph = graph_builder.compile()

graph.invoke({
    "reiseziel": "Rom",
    "tage": 3,
    "budget": 600
})