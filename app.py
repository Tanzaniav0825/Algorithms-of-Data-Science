import sys

from pathlib import Path

import streamlit as st

# Directory where streamlit_app.py lives: /app/src
BASE_DIR = Path(__file__).resolve().parent
PARENT_DIR = BASE_DIR.parent  # /app

# Make sure both /app/src and /app are on sys.path
for p in (BASE_DIR, PARENT_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

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
    # map name -> full persona dict
    persona_options = {p["name"]: p for p in personas}

    selected_persona_names = st.sidebar.multiselect(
        "Select personas",
        list(persona_options.keys()),
        default=list(persona_options.keys())[:1],
    )
    selected_personas = [persona_options[name] for name in selected_persona_names]

    num_turns = st.sidebar.slider("Number of conversation turns", 2, 12, 4)
    temperature = st.sidebar.slider("Creativity (temperature)", 0.1, 1.0, 0.7)

    if st.button("Run Simulation"):
        if not selected_personas:
            st.warning("Please select at least one persona.")
            return

        with st.spinner("Running simulation..."):
            try:
                # NOTE: call matches the new simulation.run_simulation signature
                result = run_simulation(
                    scenario=scenario,
                    personas=selected_personas,
                    num_turns=num_turns,
                    temperature=temperature,
                )
            except Exception as e:
                st.error(f"Simulation failed: {e}")
                return

        st.subheader("Summary")
        st.metric("Acceptance Score", f"{result['acceptance_score']} / 100")

        engine = result.get("engine", "unknown")
        st.caption(f"Engine used: {engine}")

        if engine == "fallback":
            st.info(
                "Simulation is running in fallback mode "
                "(local deterministic engine). "
                "TinyTroupe / OpenAI is not active in this environment."
            )
        elif engine == "tinytroupe":
            st.success("Simulation is running via TinyTroupe persona agents.")

        st.write("### Positive Signals")
        for sig in result.get("positive_signals", []):
            st.write(f"- {sig}")

        st.write("### Risks & Concerns")
        for risk in result.get("risks", []):
            st.write(f"- {risk}")

        st.write("### Transcript")
        st.markdown(result.get("transcript", ""))
    
if __name__ == "__main__":
    main()
