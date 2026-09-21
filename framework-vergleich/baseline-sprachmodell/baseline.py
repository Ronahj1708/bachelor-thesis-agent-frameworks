import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": (
                "Erstelle einen personalisierten Reiseplan.\n\n"
                "Reiseziel: Rom\n"
                "Reisedauer: 3 Tage\n"
                "Budget: 600 Euro\n"
                "Interessen: Kultur, Sehenswürdigkeiten und italienisches Essen\n\n"
                "Erstelle daraus einen strukturierten Reiseplan für jeden Tag."
            )
        }
    ]
)

print(response.choices[0].message.content)