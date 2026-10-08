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
    interessen: str
    reiseplan_text: str
    versuche: int
    freigegeben: bool


def begruessung(state: ReiseState):
    print("Willkommen!")
    print(f"Reiseziel: {state['reiseziel']}")
    print(f"Tage: {state['tage']}")
    print(f"Budget: {state['budget']} €")
    print(f"Interessen: {state['interessen']}")

    return state


def reiseplan(state: ReiseState):
    print("Ich erstelle jetzt deinen Reiseplan.")

    prompt = (
        "Erstelle einen personalisierten Reiseplan.\n\n"
        f"Reiseziel: {state['reiseziel']}\n"
        f"Reisedauer: {state['tage']} Tage\n"
        f"Budget: {state['budget']} Euro\n"
        f"Interessen: {state['interessen']}\n\n"
        "Erstelle daraus einen strukturierten Reiseplan für jeden Tag."
    )

    response = llm.invoke(prompt)

    state["reiseplan_text"] = response.content

    return state


def budget_pruefen(state: ReiseState):
    text = state["reiseplan_text"]
    zeilen = text.split("\n")

    gesamt_zeile = ""
    for zeile in zeilen:
        if "Gesamt" in zeile:
            gesamt_zeile = zeile

    zahl_gerade = ""
    zahlen = []
    for zeichen in gesamt_zeile:
        if zeichen.isdigit():
            zahl_gerade = zahl_gerade + zeichen
        else:
            if zahl_gerade != "":
                zahlen.append(int(zahl_gerade))
                zahl_gerade = ""
    if zahl_gerade != "":
        zahlen.append(int(zahl_gerade))

    if zahlen:
        summe = max(zahlen)
    else:
        summe = 0

    print(f"Erkannte Summe: {summe} €")

    if summe <= state["budget"]:
        state["freigegeben"] = True
    elif state["versuche"] >= 2:
        state["freigegeben"] = True
    else:
        state["freigegeben"] = False
        state["versuche"] += 1

    return state


def ausgabe(state: ReiseState):
    print("\nDein Reiseplan:")
    print(state["reiseplan_text"])

    return state


graph_builder = StateGraph(ReiseState)

graph_builder.add_node("begruessung", begruessung)
graph_builder.add_node("reiseplan", reiseplan)
graph_builder.add_node("budget_pruefen", budget_pruefen)
graph_builder.add_node("ausgabe", ausgabe)

graph_builder.add_edge("begruessung", "reiseplan")
graph_builder.add_edge("reiseplan", "budget_pruefen")


def naechster_schritt(state: ReiseState):
    if state["freigegeben"]:
        return "ausgabe"
    else:
        return "reiseplan"


graph_builder.add_conditional_edges("budget_pruefen", naechster_schritt)

graph_builder.set_entry_point("begruessung")
graph_builder.set_finish_point("ausgabe")

graph = graph_builder.compile()


graph.invoke({
    "reiseziel": "Rom",
    "tage": 3,
    "budget": 600,
    "interessen": "Kultur, Sehenswürdigkeiten und italienisches Essen",
    "versuche": 0
})