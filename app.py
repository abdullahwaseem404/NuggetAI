from flask import Flask, request, jsonify
import os
from google import genai
from dotenv import load_dotenv
from backend.rag_pipeline import retrieve_context
load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello"
)

print(response.text)
SYSTEM_PROMPT = """
You are an academic AI assistant.

- Explain step-by-step
- Use simple language
- Define technical terms
- Stay factual
"""

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("query")

    context = retrieve_context(query)

    full_prompt = f"""
    Context:
    {context}

    Question:
    {query}

    Answer step-by-step:
    """

    try:
        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
            SYSTEM_PROMPT + full_prompt
        )
        return jsonify({"answer": response.text})
    except Exception as e:
        return jsonify({"error": str(e)})