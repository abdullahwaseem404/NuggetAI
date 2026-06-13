# 🤖 NuggetAI

### Academic AI Chatbot for Tech Students

A **Flask + Streamlit + Gemini-powered academic chatbot** designed to help tech students understand concepts clearly using **RAG (Retrieval-Augmented Generation)**, step-by-step explanations, and simple language.

---

## 🚀 Features

* 🎓 Academic-focused AI assistant for technical subjects
* 🧠 Step-by-step explanations using Gemini models
* 📚 RAG-based context retrieval from local knowledge base
* ❓ Intelligent responses with clarifications when needed
* 🧾 Simple definitions of technical terms
* 💻 Flask backend API + Streamlit frontend
* 🔐 Secure API key management using `.env`
* 📊 Basic evaluation module (accuracy & F1 score)

---

## 🧱 Project Architecture

```
Frontend (Streamlit)
        ↓
Flask API (/chat endpoint)
        ↓
RAG Pipeline (FAISS + embeddings)
        ↓
Gemini Model (Google Generative AI)
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/abdullahwaseem404/NuggetAI.git
cd NuggetAI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=YOUR_GEMINI_KEY_HERE
```

---

## ▶️ Running the Project

### Option 1: Run full system (recommended)

```bash
python run.py
```

This will start:

* Flask backend (port 5001)
* Streamlit frontend

---

### Option 2: Run manually

#### Start backend:

```bash
python backend/api.py
```

#### Start frontend:

```bash
streamlit run app.py
```

---

## 🔌 Backend API (Flask)

### Endpoint

```
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
  "answer": "Step-by-step explanation from Gemini..."
}
```

---

## 🧠 RAG Pipeline

Located in `backend/rag_pipeline.py`

### Workflow:

1. Load knowledge base (`knowledge.txt`)
2. Split into chunks
3. Convert into embeddings (FAISS vector store)
4. Retrieve top-k relevant chunks
5. Inject into Gemini prompt

### Key Function:

```python
retrieve_context(query)
```

---

## 📊 Evaluation Module

File: `evaluator.py`

### Metrics:

* Accuracy
* F1 Score

```python
evaluate_model(true_answers, predicted_answers)
```

---
