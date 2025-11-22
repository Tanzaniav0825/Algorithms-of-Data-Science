import json
from pathlib import Path
from typing import List, Dict, Any

# This file lives in the repo root, so data/ is a sibling directory.
DATA_DIR = Path(__file__).resolve().parent / "data"
PERSONA_FILE = DATA_DIR / "personas.json"

REQUIRED_FIELDS = [
    "id",
    "name",
    "tech_skill_level",
    "usage_context",
    "goals",
    "frustrations",
    "scenario_tags",
]


def _validate_persona(p: Dict[str, Any]) -> None:
    """Basic validation to ensure personas are usable and consistent."""
    missing = [f for f in REQUIRED_FIELDS if f not in p or not p[f]]
    if missing:
        raise ValueError(
            f"Persona {p.get('id', p.get('name', 'UNKNOWN'))} missing fields: {missing}"
        )

    if p["tech_skill_level"] not in {"beginner", "intermediate", "advanced", "expert"}:
        raise ValueError(
            f"Persona {p['id']} has invalid tech_skill_level={p['tech_skill_level']}"
        )

    if not isinstance(p["goals"], list) or not isinstance(p["frustrations"], list):
        raise ValueError(
            f"Persona {p['id']} must have list fields for goals and frustrations."
        )

    if not isinstance(p["scenario_tags"], list) or not p["scenario_tags"]:
        raise ValueError(
            f"Persona {p['id']} must have at least one scenario_tag."
        )


def load_personas() -> List[Dict[str, Any]]:
    """
    Load personas from data/personas.json and validate them.
    Raises a clear error if the file is missing or invalid.
    """
    if not PERSONA_FILE.exists():
        raise FileNotFoundError(f"Persona file not found: {PERSONA_FILE}")

    with PERSONA_FILE.open("r", encoding="utf-8") as f:
        personas = json.load(f)

    if not isinstance(personas, list):
        raise ValueError("personas.json must contain a JSON array of persona objects.")

    for p in personas:
        _validate_persona(p)

    return personas

