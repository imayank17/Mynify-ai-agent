# Mynify AI Agent

![Status](https://img.shields.io/badge/status-production-brightgreen)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-supported-orange)
![License](https://img.shields.io/badge/license-TBD-lightgrey)

## 🔥 Mynify AI Agent
**Conversational agentic AI for intelligent multi-threaded chat, resume-aware responses, and document-backed retrieval.**

---

## 📌 Overview
Mynify AI Agent is a production-ready conversational AI system built with LangGraph, LangChain, and Streamlit. It supports multi-turn chat, thread-aware history, retrieval-augmented generation (RAG), tool execution, and PDF-aware workflows — all designed for a modern AI agent experience.

---

## 🧠 Key Features
- Multi-turn conversational chatbot with persistent thread history
- Thread-based chat management and conversation switching
- RAG pipeline for PDF document ingestion and context-aware answers
- Agentic workflow support via LangGraph graph execution
- Tool integration: web search, stock lookup, and custom retrieval tools
- Streamlit frontend for fast UI iteration and usability
- SQLite-backed conversation checkpointing for observability and persistence
- Resume-aware and context-preserving responses across chat turns

---

## 🏗️ Architecture
Mynify AI Agent separates the system into front-end and backend components:

- `app.py` and `frontend.py` provide Streamlit-based interfaces
- `langgraph_backend.py` contains the LangGraph state machine, tool orchestration, and multi-threaded chat persistence
- `rag_backend.py` powers PDF ingestion, FAISS retrieval, and context-aware RAG responses
- `chatbot.db` stores LangGraph checkpoints and thread state
- Streamlit handles UI, thread switching, new chat creation, and live response streaming

The system routes user messages through a LangGraph state graph, optionally invokes tools, and persists conversation state per thread for seamless context recovery.

---

## ⚙️ Tech Stack
- LangGraph
- LangChain
- OpenAI-compatible models via OpenRouter
- Streamlit UI
- SQLite checkpoint storage
- FAISS vector store for retrieval
- Python 3.11+
- dotenv for environment config

---

## 📂 Project Structure
- `app.py` — primary Streamlit chatbot UI using `langgraph_backend.py`
- `frontend.py` — PDF-aware Streamlit interface for RAG-enabled chat
- `langgraph_backend.py` — core LangGraph graph, tool integration, thread checkpointing
- `rag_backend.py` — RAG pipeline, PDF ingestion, FAISS retrievers, and tool definitions
- `requirements.txt` — dependency manifest
- `chatbot.db` — SQLite state persistence for chat threads
- `.streamlit/` — Streamlit configuration files
- `venv/` — local Python virtual environment

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment
Create a `.env` file at the project root:
```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

### 3. Run the app
Choose one of the Streamlit frontends:
```bash
streamlit run app.py
```

Or run the RAG-enabled frontend:
```bash
streamlit run frontend.py
```

---

## 🧪 Example Usage
1. Open the Streamlit app in your browser.
2. Start a new conversation or select an existing thread.
3. Type a question into the chat prompt.
4. The assistant responds using LangGraph and tool-backed reasoning.
5. Upload a PDF in `frontend.py` to enable document-aware retrieval.
6. Use the sidebar to switch threads and continue prior conversations.

---

## 📸 Screenshots
> Add screenshots here once available

- `screenshot-1.png` — main chat view
- `screenshot-2.png` — thread selector and history
- `screenshot-3.png` — PDF ingestion / RAG workflow
- `screenshot-4.png` — tool execution feedback

---

## 🔐 Environment Variables
- `OPENROUTER_API_KEY` — API key for OpenRouter-backed LLM and embeddings

> Add additional variables or secret keys here as needed for deployment.

---

## 📈 Future Improvements
- Add REST API endpoints for programmatic access
- Implement user authentication and workspace isolation
- Improve memory and long-term context management
- Add richer tool plugins and external knowledge sources
- Replace local checkpoint DB with managed cloud storage
- Extend support for more document types and embeddings backends

---

## 🤝 Contributing
Contributions and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with clear changelog notes
4. Keep changes modular and maintain production-readiness

---

## 📄 License
Add a `LICENSE` file to define the project license and terms.

---

## 🙌 Acknowledgements
- LangGraph for agentic workflow orchestration
- LangChain for conversational AI primitives
- Streamlit for rapid frontend development
- OpenRouter / OpenAI-compatible models for generative capabilities
