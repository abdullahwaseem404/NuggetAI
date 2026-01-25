# 🤖 NuggetAI
# Academic AI Chatbot
### For Tech Students – Concepts, Models, and Limitations

Working Demo: https://www.youtube.com/watch?v=-CM5lSlJ6tc

An academic-focused chatbot built with **Streamlit** and **Google Generative AI (Gemini)**.  
This project is designed to help **tech students** learn concepts step-by-step, with clear explanations, factual answers, and safe guidance when uncertainty arises.

---

## 🚀 Features
- 🎓 Academic-focused assistant tailored for tech students.
- ✅ Factual answers with step-by-step explanations.
- ❓ Asks clarifying questions when queries are unclear.
- 🧾 Defines technical terms in simple language.
- ⚠️ Provides safe suggestions when unsure.
- 💻 Interactive **Streamlit Web App** interface.
- 🔑 Secure API key management with **python-dotenv**.

---

## 📂 Project Structure
```
├── app.py              # Streamlit chatbot app
├── .env                # Environment file containing GEMINI_API_KEY
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/abdullahwaseem404/NuggetAI.git
```
```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file in the project root and add your Gemini API key:

```
GEMINI_API_KEY=YOUR_GEMINI_KEY_HERE
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the app in your browser. You’ll see a chatbot interface where you can ask academic questions.

---
