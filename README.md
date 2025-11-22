🧠 Persona-Based AI Feedback Simulator
Production-Ready Streamlit App with TinyTroupe Integration
This project delivers a fully functional, deployable AI simulation tool designed to streamline product feedback collection using persona-based AI conversations. It provides realistic user feedback simulations for product teams, enabling rapid iteration on UX and feature design.
This app uses:
Streamlit for UI
TinyTroupe (OpenAI personas) for AI agent simulation
Hugging Face Spaces for deployment
Dockerfile for reproducible builds
Persona database for customizable user archetypes
Simulation engine to generate multi-turn conversations
End-to-end testing & monitoring setup
🚀 Features
✅ Persona-Based Feedback Simulation
Generates realistic feedback conversations using predefined personas.
Adjustable:
Number of turns
Creativity
Target feature or user scenario
✅ TinyTroupe AI Engine
Uses OpenAI-compatible API to generate agentic persona behavior
Falls back gracefully to a default response if API key is missing
✅ Production Deployment
Fully deployable on Hugging Face Spaces
Includes:
Dockerfile
requirements.txt
App entrypoint (streamlit_app.py)
Automatic builds
Error handling in UI
✅ Persona Database
Expandable JSON dataset of personas
Includes demographics, expertise levels, goals, frustrations, and behavior profiles
Loaded dynamically via persona_loader.py
✅ Clean Architecture
All Python logic lives in the root directory, including:
streamlit_app.py — main UI
simulation.py — simulation engine
persona_loader.py — JSON persona loader
personas.json — persona database
✅ Testing
Includes basic runtime test: test_streamlit.py
Validates app import and persona loading
📁 Project Structure
Algorithms-of-Data-Science/
│
├── streamlit_app.py        # Main Streamlit UI
├── simulation.py           # TinyTroupe-based simulation engine
├── persona_loader.py       # Loads personas.json
├── personas.json           # Persona database
│
├── requirements.txt        # Python dependencies
├── Dockerfile              # For HuggingFace deployment
├── README.md               # (this file)
│
├── data/                   # Optional (not required for app)
└── docs/
     └── TECH_REPORT.md     # Documentation for course deliverables
💻 Local Development
1️⃣ Create and activate your environment
conda create -n simulator python=3.12 -y
conda activate simulator
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the application
streamlit run streamlit_app.py
The app will open automatically in your browser.
🔐 TinyTroupe / OpenAI API Configuration
The simulation engine supports TinyTroupe-style AI personas via OpenAI-compatible API keys.
To enable full persona simulations:
Set your API key in your environment:
MacOS / Linux:
export OPENAI_API_KEY="your-key-here"
Windows PowerShell:
$env:OPENAI_API_KEY="your-key-here"
If no key is supplied, the app gracefully uses a fallback engine and displays:
Engine used: fallback
🌐 Deployment on Hugging Face
1️⃣ Create a new Space
Choose:
SDK: Docker
Runtime: CPU Basic
Visibility: Public (or private)
2️⃣ Upload these required files:
Dockerfile
requirements.txt
streamlit_app.py
simulation.py
persona_loader.py
personas.json
3️⃣ Hugging Face builds automatically
Watch the “Build Logs” for success:
Your app is running at: https://huggingface.co/spaces/<username>/<space-name>
4️⃣ App auto-restarts if files change
The app handles:
Missing persona file errors
JSON decode errors
Import issues
Missing API key
🤖 Persona Database (personas.json)
Each persona includes:
{
  "id": "tech_savvy_user",
  "name": "Jordan",
  "age": 29,
  "skill_level": "advanced",
  "goals": ["efficiency", "automation"],
  "frustrations": ["slow UI"],
  "tone": "direct",
  "scenario_preferences": ["quick share", "dashboard customization"]
}
You can add unlimited personas — the system loads them dynamically.
🧪 Testing
Run the basic import test:
python test_streamlit.py
This verifies:
Streamlit app loads
Persona JSON is valid
Simulation engine initializes
📊 Performance, Monitoring & Reliability
The deployed app includes:
✔ Streamlit runtime logging
✔ Hugging Face build logs
✔ API fallback if OpenAI credentials missing
✔ Error blocking for:
Missing files
Broken JSON
Missing persona fields
✔ Production Docker image ensuring:
Consistent environment
Reproducible builds
Secure dependency confinement
📈 Real-World Use Cases
UX Research teams testing new feature flows
Product managers simulating user responses
Data science teams generating synthetic feedback datasets
Students learning persona-driven AI interfaces
Early-stage startups replacing expensive focus groups
✨ Future Enhancements
Save conversation transcripts
Multi-persona group simulations
Persona “mood variability”
Export results to CSV
Real-time analytics dashboard
👩‍💻 Author
Tanzania Vernon
Master’s in Data Science — Pace University
AI | Machine Learning | UX Simulation | Product Analytics
GitHub: https://github.com/Tanzaniav0825
LinkedIn: https://www.linkedin.com/in/tanzania-vernon-0a0a14343
