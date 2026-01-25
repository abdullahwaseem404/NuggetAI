import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("❌ GEMINI_API_KEY not found in .env file.")
    st.stop()

os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

st.set_page_config(
    page_title="Academic AI Chatbot",
    layout="centered",
    page_icon="🤖"
)

st.title("🤖 Academic AI Chatbot")
st.caption("For Tech Students – concepts, models, and limitations")

SYSTEM_PROMPT = """
You are an academic-focused AI assistant for Tech students.

Rules:
1) Give factual answers and do not invent data.
2) If the question is unclear, ask one short clarifying question.
3) Explain step-by-step when teaching.
4) Use simple language and define technical terms.
5) If you are not sure, say so and suggest a safe way to verify.
6) Keep answers short unless asked for detail.
"""

@st.cache_resource(show_spinner=False)
def load_gemini():
    return genai.Client(api_key=GEMINI_API_KEY)

gemini_client = load_gemini()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form("chat_form"):
    user_query = st.text_input(
        "Ask a question:"
    )
    ask_btn = st.form_submit_button("Ask")

    if ask_btn:
        if not user_query.strip():
            st.warning("Please type a question.")
        else:
            full_prompt = SYSTEM_PROMPT + "\nUser: " + user_query
            try:
                response = gemini_client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=full_prompt
                )
                answer = (response.text or "").strip()
            except Exception as e:
                answer = f"Error: {e}"

            st.session_state.chat_history.append((user_query, answer))

for q, a in reversed(st.session_state.chat_history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")
    st.markdown("---")