import os
import requests
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="NuggetAI", page_icon="🎓")
st.title("NuggetAI")
st.caption("Ask technical questions and get clear, step-by-step explanations.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("What would you like to learn?")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
    try:
        result = requests.post(
            os.getenv("NUGGETAI_API_URL", "http://127.0.0.1:5001/chat"),
            json={"query": query},
            timeout=60,
        )
        result.raise_for_status()
        answer = result.json().get("answer", "No answer returned.")
    except requests.RequestException as error:
        answer = f"The backend is unavailable: {error}"
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)