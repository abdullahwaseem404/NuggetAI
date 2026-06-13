from flask import Flask, request, jsonify
import os
from google import genai
from dotenv import load_dotenv
from backend.rag_pipeline import retrieve_context

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("query")

    context = retrieve_context(query)

    prompt = f"""
Context:
{context}

Question:
{query}

Explain step by step.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return jsonify({"answer": response.text})


if __name__ == "__main__":
    print("Flask running...")
    app.run(port=5001, debug=False, use_reloader=False)