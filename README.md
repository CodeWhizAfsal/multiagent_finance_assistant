# 🧠 Multi-Agent Voice-Enabled Financial Assistant

A multi-source, multi-agent finance assistant that delivers **spoken market briefings** every morning. Built as a **monorepo** integrating FastAPI microservices and a Streamlit frontend, this assistant ingests data from APIs and filings, performs RAG (Retrieval-Augmented Generation), and communicates via voice using Whisper + TTS pipelines.

## 🎯 Use Case

Every trading day at 8 AM, a portfolio manager asks:

> “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”

The assistant responds verbally:

> “Today, your Asia tech allocation is 22% of AUM, up from 18% yesterday.  
TSMC beat estimates by 4%, Samsung missed by 2%.  
Regional sentiment is neutral with a cautionary tilt due to rising yields.”

---

## 🧱 Architecture Overview

### 🧠 Agent Roles

| Agent          | Role                                                                 |
|----------------|----------------------------------------------------------------------|
| **API Agent**     | Pulls real-time and historical market data (Yahoo Finance)         |
| **Scraping Agent** | Extracts financial reports and earnings surprises (BeautifulSoup) |
| **Retriever Agent**| FAISS-powered semantic search across indexed documents            |
| **Analysis Agent** | Analyzes exposure/risk, detects trends, and summarizes findings   |
| **Language Agent** | Synthesizes narrative using OpenAI's GPT + LangGraph               |
| **Voice Agent**    | Handles STT (Whisper) and TTS (TTSModels/pyttsx3)                 |

---

## 🔁 Data Flow

```plaintext
User Voice Input 🎤
       ↓
[Voice Agent] → Whisper STT
       ↓
[Orchestrator (FastAPI)]
       ↓
[Retriever Agent] → FAISS → Top-k Docs
       ↓
[Language Agent] → LLM (GPT) → Market Summary
       ↓
[Voice Agent] → TTS
       ↓
Spoken Market Brief 🗣️ 
```
# 💻 Finance Assistant – Multi-Agent Voice-Enabled Financial Assistant

A multi-agent financial assistant that delivers daily market briefings using LLMs, scraping, RAG, and voice interaction. Built using **FastAPI**, **Streamlit**, and **LangGraph**.

---

## 📁 Project Structure (Monorepo)

```
finance-assistant/
│
├── app/
│   ├── orchestrator.py          # FastAPI router coordinating all agents
│   ├── agents/
│   │   ├── api_agent.py
│   │   ├── scraper_agent.py
│   │   ├── retriever_agent.py
│   │   ├── analysis_agent.py
│   │   └── language_agent.py
│
├── voice/
│   ├── whisper_stt.py
│   ├── tts_generator.py
│
├── streamlit_app/
│   └── streamlit_app.py         # Streamlit frontend interface
│
├── data_ingestion/
│   └── document_loader.py       # Loads filings for indexing
│
├── faiss_index/
│   └── indexer.py
│
├── Dockerfile
├── requirements.txt
├── Procfile
├── runtime.txt
└── README.md
```

## 🚀 Deployment

### 🔹 FastAPI Backend (Heroku)

**Build Docker image:**
```bash
docker build -t market-briefing-api .
```

**Push to Heroku:**
```bash
git push heroku main
```

**URL:** `https://your-heroku-app.herokuapp.com`

---

### 🔹 Streamlit Frontend (Streamlit Cloud)

- Link GitHub repo
- Set main file: `streamlit_app/streamlit_app.py`

**URL:** `https://your-streamlit-app.streamlit.app`

---

## 🧰 Tools & Frameworks

| Category     | Tools Used                                 |
|--------------|---------------------------------------------|
| LLM          | OpenAI GPT, LangGraph                      |
| RAG          | FAISS + OpenAI Embeddings                  |
| Voice        | Whisper (STT), pyttsx3 / TTSModels (TTS)   |
| Data Sources | Yahoo Finance, Company Filings             |
| Backend      | FastAPI, Uvicorn, Gunicorn                 |
| Frontend     | Streamlit                                  |
| Deployment   | Heroku (FastAPI), Streamlit Cloud          |
| Orchestration| Custom router with fallback mechanism      |

---

## 📜 Setup Instructions (Local)

```bash
git clone https://github.com/your-username/finance-assistant.git
cd finance-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI backend
uvicorn app.orchestrator:app --reload --host 0.0.0.0 --port 8000

# In another terminal
cd streamlit_app
streamlit run streamlit_app.py
```

---

## 📓 AI Tool Usage Log

See `docs/ai_tool_usage.md` for:

- Prompt engineering strategies  
- LLM response logs  
- Model parameter settings  
- Embedding vector setup and tuning  

---

## 📊 Performance Benchmarks

| Component       | Avg. Latency |
|------------------|---------------|
| Whisper STT      | ~1.5 sec      |
| Retrieval (FAISS)| < 100 ms      |
| GPT Response     | ~2.0 sec      |
| TTS Output       | ~0.8 sec      |

---

## 🧠 Future Improvements

- 📈 Add streaming output with partial speech responses  
- 🧩 Integrate Pinecone for scalable vector search  
- 📡 Webhook for auto-market-brief delivery at 8 AM daily  
- 🧍 Persona tuning for portfolio managers  

---

## 🔗 Demo URLs

- 🌐 **Streamlit App:** [streamlit.io/your-app](https://streamlit.io/your-app)  
- 🚀 **Heroku API:** [your-api.herokuapp.com](https://your-api.herokuapp.com)

---

## 👨‍💻 Author

**Afsal Majeed**  
📧 majeedafsal00@gmail.com  
📎 [LinkedIn]([https://www.linkedin.com/in/your-profile/](https://www.linkedin.com/in/afsal-majeed-997ba81b9/))


