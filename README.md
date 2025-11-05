  
### *Agentic AI Persona Simulation with TinyTroupe Framework*

---

## 📘 Overview  
This branch (`capstone2-d2`) contains the **beta version** of the persona-simulation app for Deliverable 2.  
It extends the TinyTroupe investigation from Deliverable 1 into a working prototype that demonstrates how **agentic AI personas** simulate realistic user feedback for feature evaluation.

**Key Objectives**
- Integrate TinyTroupe-style persona configuration into a Python / Streamlit workflow  
- Build a modular pipeline → `compiler → simulator → synthesis → evaluation → logs`  
- Produce quantitative scoring (clarity, efficiency, safety, accessibility, trust)  
- Provide reproducible documentation for instructor review  

---

## 🧱 Repository Structure  

| Path | Description |
|------|--------------|
| `core/` | Source modules for compiler, simulator, synthesis, evaluation |
| `app/` | Streamlit UI (beta demo) |
| `docs/TECH_REPORT.md` | Full Deliverable 2 Technical Report |
| `logs/` | JSONL and CSV logs from runs |
| `README.md` | Deliverable 2 summary (this file) |

---

## 🧩 System Highlights  
- **Personas:** Busy Parent, Tech-Savvy User, Accessibility Reviewer, First-Time User, Privacy Skeptic  
- **Simulation Flow:** Feature → Prompt → 3-turn dialogue → Synthesis → Evaluation  
- **Evaluation Metrics:** Weighted scores + acceptance (0–100)  
- **Logging:** Automatic JSONL transcripts and CSV summaries  
- **Extensibility:** Prepared for TinyTroupe LLM integration in Deliverable 3  

---

## 🧠 How to Run  
```bash
pip install -r requirements.txt
streamlit run app/ui_streamlit.py

