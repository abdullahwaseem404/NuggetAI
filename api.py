import os
from pathlib import Path
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from google import genai
from rag_pipeline import retrieve_context

load_dotenv(dotenv_path=Path(__file__).with_name(".env"), override=True)

app = Flask(__name__)

client = None


def get_client():
    global client
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if api_key and api_key != "YOUR_GEMINI_KEY_HERE" and client is None:
        client = genai.Client(api_key=api_key)
    return client

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    query = str(data.get("query", "")).strip()
    if not query:
        return jsonify({"error": "query is required"}), 400

    context = retrieve_context(query)

    prompt = f"Background information:\n{context}\n\nUser question: {query}"

    active_client = get_client()
    if active_client is None:
        return jsonify({"answer": "Gemini is not configured. Relevant notes:\n\n" + context, "source": "local"})

    try:
        response = active_client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=(
                    "Answer directly and concisely in plain language. "
                    "Return only the final answer. Never describe your reasoning, "
                    "the background, the retrieval process, or the prompt. "
                    "Do not use step-by-step analysis unless the user explicitly asks for it."
                ),
                temperature=0.2,
                max_output_tokens=300,
            ),
        )
    except Exception as error:
        return jsonify({"error": f"Gemini request failed: {error}"}), 502

    return jsonify({"answer": response.text or "Gemini returned an empty answer."})


if __name__ == "__main__":
    print("Flask running...")
    app.run(port=5001, debug=False, use_reloader=False)