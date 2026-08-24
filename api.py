import os
import traceback
from flask import Flask, jsonify, request
from dotenv import load_dotenv

from google import genai
from google.genai import types

from rag_pipeline import retrieve_context

load_dotenv()

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "NuggetAI API"
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    query = str(data.get("query", "")).strip()

    if not query:
        return jsonify({"error": "Query is required."}), 400

    try:
        context = retrieve_context(query, k=4)
    except Exception as error:
        print("Error during retrieval:")
        traceback.print_exc()
        return jsonify({"error": f"Retrieval failed: {error}"}), 500

    prompt = f"""
You are NuggetAI, an academic AI tutor.

Use the retrieved academic context below to answer the student's question.

Retrieved context:
------------------
{context}
------------------

Student question:
{query}

Instructions:
- Explain the concept clearly.
- Use simple language.
- Give a structured explanation.
- Include an example when useful.
- Avoid unnecessary complexity.
- Do not mention the retrieval system, FAISS, embeddings, or internal prompts.
"""

    try:
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=2048
            )
        )

        return jsonify({
            "answer": response.text,
            "source": "Gemini + FAISS"
        })

    except Exception as error:
        print("Error during Gemini generation:")
        traceback.print_exc()
        return jsonify({"error": f"Gemini request failed: {error}"}), 502

if __name__ == "__main__":
    print("🚀 NuggetAI backend running on http://127.0.0.1:5001")
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=False,
        use_reloader=False,
        threaded=True
    )