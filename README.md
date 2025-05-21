# Agentic Weather Assistant

A lightweight, interactive weather chatbot built with **Gradio**, **Transformers**, and **OpenWeatherMap API**. The system simulates basic agent-like reasoning using an instruction-following model and integrates a rule-based recommendation engine for personalized weather advice. GitHub repository for the **AI and Expert Systems** course taught during the Spring Semester for the **MsC in Informatics-Computer Science** at the **Department Of Informatics- University of Piraeus,Greece**. 

---

## 📁 Project Structure
```
.
├── agentic_weather.py         # Gradio interface for user interaction
├── llmodel.py                 # Logic for LLM prompting and decision routing
├── weatherfunctionality.py    # Weather data retrieval via OpenWeatherMap API
├── recommendfunctionality.py  # Rule-based suggestion engine
├── .env                      # (Not committed) add your API keys
└── README.md                 # This file
```
---

## 🚀 How It Works

1. If the user's question includes `"weather in <city>"`, the assistant extracts the city and fetches real-time weather data.
2. If the input is ambiguous, it uses a text-to-text model (`google/flan-t5-base`) to assist and guide.
3. If is weather related (but ambiguous), it fetches the weather if a city is included in the querry. If not, it responds with a generic assistant message.
4. Rule-based recommendations are provided based on temperature and weather conditions.

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.10+
- Hugging Face `transformers` library
- Gradio
- OpenWeatherMap API key

---

### 📦 Installation

```bash
git clone https://github.com/dimitris1pana/simpleAgency.git
cd agentic-weather

pip install transformers gradio python-dotenv requests torch
```

⸻

🔐 Environment Variables

Create a .env file in the root directory with your OpenWeatherMap API key:

OPENWEATHERMAP_API_KEY="your_api_key_here"

You can get one for free at: https://openweathermap.org/api

⸻

▶️ Run the App

python agentic_weather.py

This will launch a local Gradio interface where you can chat with the assistant.

⸻

🧠 Example Prompts

Prompt	Response
“What’s the weather in London?”	Fetches weather and gives recommendations
“Is it sunny today in Rome?”	Uses model + weather API
“What can you do?”	(Generic assistant message)


⸻

📚 Technologies Used
- Transformers (Hugging Face)
- Gradio
- OpenWeatherMap API
- Python 3.10+

⸻

✅ To Do / Ideas
- Switch to a better open-source model for more accurate intent detection or general discussion and user - guidance
- Add support for free weather APIs like Open-Meteo
- Integrate a location-aware version (e.g., auto-detect city)
- Enable voice queries and text-to-speech output
    

⸻

Dr. Dimitrios P. Panagoulias
🔗 [LinkedIn](https://www.linkedin.com/in/dimitris-panagoulias-17a05217/)
