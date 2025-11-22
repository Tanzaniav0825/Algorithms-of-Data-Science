# 🧠 Persona-Based AI Feedback Simulator

## Production-Ready Streamlit App with TinyTroupe Integration

This project provides a deployable AI-driven tool for generating persona-based coversations that stimulate product feedback.

# 🚀 Features
## 🎭 Persona-Based Feedback Simulation
- Multi-turn conversation generation
- Adjustable number of turns
- Adjustable creativity level
- Selected scenarios

## 🤖 TinyTroupe AI Integration
- OpenAI-compatible API
- Automatic fallback engine if API key is missing

## ☁️ Deployment-Ready
- Hugging Face Spaces (Docker-based)
- Automatic rebuild and logs
- Handles missing files and errors gracefully

## 🧩 Extendable Persona Database
- JSON-based
- Easy to update
- Includes demographics, tone, goals, frustrations, skill levels

# 📁 Project Structure

Algorithms-of-Data-Science/
│
├── streamlit_app.py
├── simulation.py
├── persona_loader.py
├── personas.json
│
├── requirements.txt
├── Dockerfile
├── README.md
│
└── docs/
    └── TECH_REPORT.md
    
# 💻 Local Development

## 🏗️ 1. Create a Conda Environment
conda create -n simulator python=3.12 -y
conda activate simulator

## 🧩 2. Install Dependencies
pip install -r requirements.txt

## ▶️ 3. Run the App
streamlit run streamlit_app.py

# 🔐 API Configuration
## macOS / Linux
export OPENAI_API_KEY="your-key-here"

## Windows PowerShell
$env:OPENAI_API_KEY="your-key-here"

If no key is provided, the app displays:
Engine used: fallback

# 🌐 Deployment on Hugging Face
## 1. Create a New Space
- SDK: Docker
- Hardware: CPU Basic

## 2. Upload These Files
Dockerfile
requirements.txt
streamlit_app.py
simulation.py
persona_loader.py
personas.json

## 3. Build Automatically
The app will run once the build finishes.

# 🧪 Testing
Run: python test_streamlit.py
Checks:
JSON loads
Simulation engine runs
Streamlit file imports

# 👩‍💻 Author
Tanzania Vernon
Master’s in Data Science — Pace University
GitHub:
https://github.com/Tanzaniav0825
LinkedIn:
https://www.linkedin.com/in/tanzania-vernon-0a0a14343

