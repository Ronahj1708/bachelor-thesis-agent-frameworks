from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(model="openai/gpt-4.1-mini"),
    name="travel_planner",
    description="A travel planner that creates personalized travel itineraries.",
    instruction=(
        "Create personalized travel itineraries based on the user's "
        "destination, travel duration, budget and interests."
    ),
)