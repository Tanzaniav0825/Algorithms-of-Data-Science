import sys
from pathlib import Path

import streamlit as st

# ---- Make sure Python can find persona_loader.py and simulation.py ----
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from persona_loader import load_personas   # type: ignore
from simulation import run_simulation      # type: ignore


def main():
    st.title("Persona-Based Feedback Simulator")

    st.sidebar.header("Simulation Controls")

    # --- Scenario selection ---
    scenario = st.sidebar.selectbox(
        "Choose a scenario",
        [
            "quick_share_button",
            "onboarding_tooltip",
        ],
        format_func=lambda s: "Quick Share Button"
        if s == "quick_share_button"
        else "Onboarding Tooltip",
    )

    # --- Persona selection ---
    personas = load_personas()
    persona_options = {p["name"]: p["id"] for p in personas}
    selected_personas = st.sidebar.multiselect(
        "Select personas",
        list(persona_options.keys()),
        default=list(persona_options.keys())[:1],
    )
    selected_persona_ids = [persona_options[name] for name in selected_personas]

    n_turns = st.sidebar.slider("Number of conversation turns", 2, 12, 6)
    n_runs = st.sidebar.slider("Number of simulations", 1, 5, 1)

    if st.button("Run Simulation"):
        if not selected_persona_ids:
            st.warning("Please select at least one persona.")
            return

        with st.spinner("Running simulation..."):
            try:
                result = run_simulation(
                    scenario_id=scenario,
                    persona_ids=selected_persona_ids,
                    n_turns=n_turns,
                    n_runs=n_runs,
                )
            except Exception as e:
                st.error(f"Simulation failed: {e}")
                return

        st.subheader("Summary")
        st.metric("Acceptance Score", f"{result['acceptance_score']} / 100")

        st.write("### Key Themes")
        for theme in result.get("key_themes", []):
            st.write(f"- {theme}")

        st.write("### Risks & Concerns")
        for risk in result.get("risks", []):
            st.write(f"- {risk}")

        st.write("### Sample Transcript")
        for turn in result.get("transcripts", []):
            speaker = turn.get("speaker", "Unknown")
            text = turn.get("text", "")
            st.markdown(f"**{speaker.capitalize()}:** {text}")


if __name__ == "__main__":
    main()
