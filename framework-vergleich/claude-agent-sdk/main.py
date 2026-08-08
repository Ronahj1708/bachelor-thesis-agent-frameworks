import asyncio
from dotenv import load_dotenv

from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, TextBlock, query

load_dotenv()

destination = "Rom"
days = 3
budget = 600
interests = "Kultur, Sehenswürdigkeiten und italienisches Essen"


async def main():
    async for message in query(
        prompt=f"""
Erstelle einen personalisierten Reiseplan.

Reiseziel: {destination}
Reisedauer: {days} Tage
Budget: {budget} Euro
Interessen: {interests}

Erstelle daraus einen strukturierten Reiseplan für jeden Tag.
""",
        options=ClaudeAgentOptions(
            system_prompt="""
Du bist ein Reiseplaner.
Erstelle realistische und übersichtliche Reisepläne auf Basis
des Reiseziels, der Reisedauer, des Budgets und der Interessen des Nutzers.
Berücksichtige das angegebene Budget bei deinen Empfehlungen.
"""
        )
    
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)


asyncio.run(main())