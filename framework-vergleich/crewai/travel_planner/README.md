# Travel Planner

Dieses Projekt wurde mit CrewAI erstellt und dient als MVP für den Vergleich verschiedener Agenten-Frameworks im Rahmen einer Bachelorarbeit.

## Ausführen

```bash
crewai run
```

## Projektstruktur

- `agents/` – Definition des Travel-Planner-Agenten
- `crew.jsonc` – Konfiguration der Crew und der Aufgaben
- `knowledge/` – Wissensdateien für den Agenten
- `tools/` – Benutzerdefinierte Tools (optional)
- `pyproject.toml` – Projekt- und Abhängigkeitsverwaltung

## Beschreibung

Der Agent erstellt auf Basis von Reiseziel, Reisedauer, Budget und Interessen einen personalisierten Reiseplan.