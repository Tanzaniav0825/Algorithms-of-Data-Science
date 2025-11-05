# Deliverable 2 — Beta Version and Technical Report  
*(Project 2 — Agentic AI Persona Simulation with TinyTroupe Framework)*  

## 1. Overview & Objectives  
This beta version extends the initial TinyTroupe persona-simulation investigation from Deliverable 1 into a fully functional application. The prototype demonstrates how agentic AI personas can simulate realistic user feedback for feature evaluation.  

**Key Goals:**  
- Integrate TinyTroupe’s persona configuration logic into a Python/Streamlit environment.  
- Create a modular pipeline (compiler → simulator → synthesis → evaluation → logs).  
- Enable reproducible, non-API-dependent simulations using rule-based logic for offline testing.  

**Major Updates Since Deliverable 1:**  
- Expanded persona diversity (five archetypes).  
- Implemented scoring and logging framework.  
- Added synthesis and evaluation modules to quantify qualitative feedback.  
- Improved documentation and GitHub repository organization.  

---

## 2. System Architecture  
**Integrated Data Flow:**  
`TinyTroupe Personas → Feature Description → Prompt Compiler → Simulation Loop → Synthesis → Evaluation → Logs`  

| Module | File | Purpose |  
|---|---|---|  
| Schemas | `core/schemas.py` | Defines Persona & Feature models |  
| Compiler | `core/compiler.py` | Transforms TinyTroupe persona JSON + feature description into structured prompts |  
| Simulator | `core/simulator.py` | Runs rule-based multi-turn dialogue emulating TinyTroupe agent logic |  
| Synthesis | `core/synthesis.py` | Extracts strengths, issues, and risk signals from conversation |  
| Evaluation | `core/evaluation.py` | Computes quantitative scores & acceptance metric |  
| Utils | `core/utils.py` | Logs results to JSONL and CSV for further analysis |  

**Architecture Highlights:**  
- Modular Python design; each component mirrors TinyTroupe’s persona–interaction pipeline.  
- Extensible to LLM-based TinyTroupe agents for future live testing.  

---

## 3. Persona Modeling  
**Imported from TinyTroupe Concepts:** Personas as modular objects with traits, goals, and guardrails.  

| Persona | Traits | Goals | Tone |  
|---|---|---|---|  
| Busy Parent | time-constrained, risk-averse | avoid mistakes | pragmatic |  
| Tech-Savvy User | detail-oriented, speed-focused | finish tasks fast | direct |  
| Accessibility Reviewer | WCAG-focused, methodical | inclusive design | constructive |  
| First-Time User | cautious, inexperienced | understand steps | curious |  
| Privacy Skeptic | trust-but-verify | explicit consent | skeptical |  

Each persona mirrors TinyTroupe’s agentic structure (persona profile + decision heuristics + contextual memory).  

---

## 4. Simulation Design & Algorithm  
**Inputs:** Feature description + TinyTroupe-formatted persona JSON.  

**Process:**  
1. Compile prompt (compiler module).  
2. Run rule-based dialogue loop (3 turns minimum).  
3. Aggregate responses into feedback objects.  

**Outputs:** Transcript + strengths + issues + recommendations + risk score.  

The current iteration uses rule-based simulation to replicate TinyTroupe’s conversation style offline, without external API calls. A future release will integrate live TinyTroupe LLM agents for more natural dialogues.  

---

## 5. Synthesis & Evaluation  
The synthesis module extracts structured insights from multi-turn dialogues and classifies risks (Low/Medium/High). The evaluation module assigns weighted scores for: Clarity, Efficiency, Safety, Accessibility, and Trust.  

| Dimension | Score (0–5) | Weight |  
|---|---|---|  
| Clarity | 4.6 | 0.22 |  
| Efficiency | 4.8 | 0.22 |  
| Safety | 4.2 | 0.22 |  
| Accessibility | 4.0 | 0.18 |  
| Trust | 3.9 | 0.16 |  
| **Acceptance** | **89 / 100** | — |  

---

## 6. Use Case Example — *Quick Share Button*  

**Persona:** Busy Parent  
**Feature:** Quick Share Button (Mobile Feed)  

**Outcome:**  
- Appreciated one-tap efficiency.  
- Flagged “accidental share” and “ambiguous icon.”  
- Recommended visible Undo and text labels.  

**Sample Transcript:**  
> **Turn 1:** “As Busy Parent, my first impression of ‘Quick Share Button’ is positive if it helps me avoid mistakes with minimal friction.”  
> **Turn 2:** “Top issues I'm noticing: accidental share; ambiguous icon; need Undo.”  
> **Turn 3:** “Suggested fixes: add Undo within 5 seconds, clarify icon label. Recommendation: Ship with fixes.”  

**CSV Snapshot:**  
Risk level = Medium, Acceptance = 86 / 100.  

---

## 7. Instructor Feedback (Round 2)  
Feedback from Deliverable 1 (TinyTroupe Phase):  
> *“Demonstrate live persona simulation and expand evaluation criteria.”*  

**Actions Taken:**  
- Implemented quantitative scoring and acceptance calculation.  
- Expanded personas to five diverse archetypes.  
- Added JSONL logging and summary exports.  
- Enhanced documentation and readability of output.  

---

## 8. Design Decisions & Trade-offs  
- Used TinyTroupe persona format for consistency with previous research.  
- Chose Python + Streamlit for transparency and reproducibility.  
- Adopted rule-based simulation for deterministic results and offline testing.  
- Deferred full LLM integration to Deliverable 3 to control complexity and cost.  

---

## 9. Future Enhancements  
- Integrate **TinyTroupe LLM engine** for natural, context-aware dialogue.  
- Enable multi-persona comparative dashboards.  
- Automate usability heuristics (e.g., WCAG and cognitive load metrics).  
- Export feedback directly to design sprint documents or issue trackers.  

---

## 10. How to Run  
```bash
pip install -r requirements.txt  
streamlit run app/ui_streamlit.py
