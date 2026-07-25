from typing import TypedDict

from langgraph.graph import StateGraph


class ReiseState(TypedDict):
    reiseziel: str
    tage: int
    budget: int


def begruessung(state: ReiseState):
    print("Willkommen!")
    print(f"Reiseziel: {state['reiseziel']}")
    print(f"Tage: {state['tage']}")
    print(f"Budget: {state['budget']} €")

    return state

def reiseplan(state: ReiseState):
    print("Ich erstelle jetzt deinen Reiseplan.")
    return state

graph_builder = StateGraph(ReiseState)

graph_builder.add_node("begruessung", begruessung)
graph_builder.add_node("reiseplan", reiseplan)

graph_builder.add_edge("begruessung", "reiseplan")

graph_builder.set_entry_point("begruessung")
graph_builder.set_finish_point("reiseplan")

graph = graph_builder.compile()

graph.invoke({
    "reiseziel": "Rom",
    "tage": 3,
    "budget": 600
})