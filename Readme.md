# 🩺 Medical Voice Chatbot MVP (RAG + Ollama + Streamlit)

This project is an MVP (Minimum Viable Product) for a **privacy-focused, voice-enabled medical chatbot**. It leverages a **Retrieval-Augmented Generation (RAG)** pipeline using **Mistral 7B via Ollama**, **ChromaDB** for vector storage, and **Streamlit** as the frontend interface.  
Voice input is supported, and the architecture is designed to easily extend to include **Digital Twin**, **caching**, and **account management** in future releases.

---

## 🚀 Features

- 🔍 **RAG Pipeline**: Answers based on a local medical knowledge base (PDF or text)
- 🧠 **LLM**: `mistral:7b` running via Ollama
- 🎤 **Voice Input**: Query the chatbot using your microphone
- 🧾 **ChromaDB**: Local vector store for embeddings
- 🌐 **Streamlit UI**: Clean, browser-based frontend
- 🧬 **Digital Twin (Planned)**: Placeholder in code for virtual patient personalization

---

## 📁 Project Structure

medical_chatbot_mvp/<br>
│<br>
├── dataIngestion/<br>
│ ├── embedding.py # Embedding logic using Sentence Transformers<br>
│ ├── extraction.py # Document loading and text extraction<br>
│ └── utils.py # Helper functions for ingestion<br>
│<br>
├── QASystem/<br>
│ ├── prompts.py # Prompt template for Ollama<br>
│ ├── tts.py # Optional text-to-speech (output audio)<br>
│ ├── voice.py # Speech-to-text handling<br>
│ ├── output.py # Text/audio output formatting<br>
│ └── utils.py # LLM and query engine wrapper<br>
│<br>
├── raw_docs/ # Folder for medical PDFs and documents<br>
│<br>
├── tests/ # Unit and integration test cases<br>
│<br>
├── utils/<br>
│ ├── exception.py # Custom error handling<br>
│ └── logger.py # Project logging setup<br>
│<br>
├── ingestion.py # Script to ingest and index documents<br>
├── main.py # Entry point for Streamlit chatbot app<br>
├── setup.py # Optional project packaging<br>
├── requirements.txt<br>
└── README.md

---

## 🔧 Requirements

- Python `>= 3.10.12`
- RAM: `>= 16GB`
- Ollama installed with `mistral:7b` pulled locally
- ChromaDB
- Streamlit

---

## 📦 Installation

```bash
# 1. Clone the repo
git clone [https://github.com/yourusername/medical-chatbot-mvp.git](https://github.com/kalalsahil/Medical_bot.git)
cd medical_chatbot_mvp

# 2. Set up virtual environment
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
python setup.py install
OR
pip install -e .

# 4. Start Ollama and pull Mistral model
ollama pull mistral

# 5. Ingest data
python ingestion.py

# 6. Test
pytest tests/

# 7. Run the chatbot
streamlit run main.py
