import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="NuggetAI",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 NuggetAI")
st.caption("Academic AI Chatbot — learn technical concepts with clear, structured explanations.")

API_URL = os.getenv("NUGGETAI_API_URL", "http://127.0.0.1:5001/chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask me a technical or academic question...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("NuggetAI is thinking..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"query": query},
                    timeout=60
                )
                response.raise_for_status()
                data = response.json()
                answer = data.get("answer", "No answer returned.")
            except requests.exceptions.ConnectionError:
                answer = "⚠️ **Backend unavailable.** Please make sure the backend is running."
            except requests.exceptions.Timeout:
                answer = "⏳ The request timed out. Please try again."
            except requests.exceptions.RequestException as error:
                answer = f"⚠️ Request failed: `{error}`"

        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})