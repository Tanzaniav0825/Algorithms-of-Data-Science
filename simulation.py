from typing import List, Dict, Any

def run_simulation(
    scenario_id: str,
    persona_ids: List[str],
    n_turns: int = 6,
    n_runs: int = 1,
) -> Dict[str, Any]:
    """
    Dummy implementation for now so UI works.
    """
    dummy_transcript = [
        {"speaker": "persona", "text": "I like the quick share button but need an undo."},
        {"speaker": "system", "text": "Thanks for the feedback!"},
    ]

    return {
        "scenario_id": scenario_id,
        "persona_ids": persona_ids,
        "acceptance_score": 78,
        "key_themes": [
            "Values speed and efficiency",
            "Wants clear labeling",
            "Concerned about accidentally sharing",
        ],
        "risks": [
            "Accidental share without undo could hurt trust",
        ],
        "transcripts": dummy_transcript,
    }

