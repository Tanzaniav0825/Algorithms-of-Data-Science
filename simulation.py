from __future__ import annotations
from typing import Any, Dict, List
import os

try:
    from tinytroupe.agent import TinyPerson
    TINYTROUPE_AVAILABLE = True
except Exception:
    TINYTROUPE_AVAILABLE = False


def _has_api_key() -> bool:
    return bool(os.getenv("OPENAI_API_KEY") or os.getenv("AZURE_OPENAI_KEY"))


def run_simulation(
    scenario: str,
    personas: List[Dict[str, Any]],
    num_turns: int = 4,
    temperature: float = 0.7,
) -> Dict[str, Any]:

    if not TINYTROUPE_AVAILABLE or not _has_api_key():
        return _fallback_simulation(scenario, personas)

    try:
        return _tinytroupe_simulation(scenario, personas, num_turns, temperature)
    except Exception as exc:
        return _fallback_simulation(
            scenario, personas, extra_note=f"TinyTroupe failed: {exc}"
        )


def _tinytroupe_simulation(
    scenario: str,
    personas: List[Dict[str, Any]],
    num_turns: int,
    temperature: float,
) -> Dict[str, Any]:

    base_prompt = (
        "You are participating in a remote product-feedback session.\n\n"
        f"FEATURE:\n{scenario}\n\n"
        "Provide honest, persona-based feedback.\n"
    )

    transcripts = []
    positives = []
    risks = []

    for p in personas:
        name = p.get("name", "Unknown User")
        tech_level = p.get("tech_skill_level")
        goals = p.get("goals")
        frustrations = p.get("frustrations")

        person = TinyPerson(name)

        if tech_level:
            person.define("tech_skill_level", tech_level)
        if goals:
            person.define("primary_goals", goals)
        if frustrations:
            person.define("pain_points", frustrations)

        persona_intro = (
            f"You are {name}. Respond ONLY as this persona.\n\n"
        )

        reply = person.listen_and_act(persona_intro + base_prompt)
        reply_txt = str(reply)

        transcripts.append(f"### {name}\n{reply_txt}")
        positives.append(f"{name}: provided useful feedback.")
        risks.append(f"{name}: raised potential concerns to investigate.")

    acceptance_score = max(50, 80 - (len(personas) - 1) * 2)

    return {
        "acceptance_score": acceptance_score,
        "positive_signals": positives,
        "risks": risks,
        "transcript": "\n\n".join(transcripts),
        "engine": "tinytroupe",
    }


def _fallback_simulation(
    scenario: str,
    personas: List[Dict[str, Any]],
    extra_note: str | None = None,
) -> Dict[str, Any]:

    persona_names = [p.get("name", "Unknown") for p in personas]

    txt = [
        "TinyTroupe is not active.",
        "Using fallback deterministic engine.",
        "",
        f"Scenario: {scenario}",
        f"Personas: {', '.join(persona_names)}",
    ]

    if extra_note:
        txt.append(f"\nNOTE: {extra_note}")

    return {
        "acceptance_score": 72,
        "positive_signals": [
            "Personas see general potential.",
            "Concept appears useful overall."
        ],
        "risks": [
            "Onboarding may confuse beginners.",
            "Privacy expectations unclear."
        ],
        "transcript": "\n".join(txt),
        "engine": "fallback",
    }


