# 🤖 NuggetAI

### Academic AI Chatbot for Tech Students

A **Flask + Streamlit + Gemini-powered academic chatbot** that helps tech students understand technical concepts using **RAG (Retrieval-Augmented Generation)**, step-by-step explanations, and simple language.

---

## 🚀 Features

* 🎓 Academic AI assistant for technical subjects
* 🧠 Step-by-step explanations powered by Gemini
* 📚 RAG-based retrieval from a local knowledge base
* 🔎 Semantic search using embeddings and FAISS
* 🧾 Simple explanations of technical concepts
* 💻 Flask backend API + Streamlit frontend
* 🔐 Secure API key management with `.env`
* 📊 Retrieval evaluation using accuracy

---

## 🧱 Project Architecture

```text
Frontend (Streamlit)
        ↓
Flask API (/chat)
        ↓
RAG Pipeline
        ↓
FAISS Vector Store
        ↓
Gemini Embeddings
        ↓
Gemini LLM
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/abdullahwaseem404/NuggetAI.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_GEMINI_KEY_HERE
GEMINI_MODEL=YOUR_GEMINI_MODEL
```

---

## ▶️ Running the Project

### Start the backend

```bash
python api.py
```

The Flask API will run on:

```text
http://127.0.0.1:5001
```

### Start the frontend

```bash
streamlit run app.py
```

Open the Streamlit URL shown in the terminal.

---

## 🔌 Backend API

### Endpoint

```text
POST /chat
```

### Request

```json
{
  "query": "What is machine learning?"
}
```

### Response

```json
{
  "answer": "Step-by-step explanation from Gemini...",
  "source": "Gemini + FAISS"
}
```

### Health Check

```text
GET /health
```

---

## 🧠 RAG Pipeline

The RAG pipeline is implemented in `rag_pipeline.py`.

### Workflow

1. Load the knowledge base
2. Split text into chunks
3. Generate text embeddings
4. Store embeddings in FAISS
5. Retrieve relevant chunks for a query
6. Provide retrieved context to Gemini
7. Generate a structured academic response

### Key Function

```python
retrieve_context(query, k=4)
```

The vector store is saved locally in:

```text
vectorstore/
```

---

## 📊 Evaluation

The project includes a simple retrieval evaluation using predefined questions and expected keywords.

### Metric

* Retrieval Accuracy

Current evaluation result:

```text
Retrieval Accuracy: 100.00%
```

---

## 🛠️ Tech Stack

* Python
* Flask
* Streamlit
* Google Gemini
* LangChain
* FAISS
* Google Generative AI Embeddings
* Jupyter Notebook
* python-dotenv

---
