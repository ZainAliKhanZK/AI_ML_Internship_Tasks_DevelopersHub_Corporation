import streamlit as st
from app import generate_response

st.set_page_config(page_title="Empathetic Companion", page_icon="💬")
st.title("💬 Empathetic Companion")
st.caption("A small fine-tuned model offering gentle, supportive responses.")

if "history" not in st.session_state:
    st.session_state.history = []

# Display past messages
for role, msg in st.session_state.history:
    st.chat_message(role).write(msg)

# New input
user_input = st.chat_input("Share what's on your mind...")

if user_input:
    st.session_state.history.append(("user", user_input))
    st.chat_message("user").write(user_input)

    with st.spinner("Thinking..."):
        response = generate_response(user_input)

    st.session_state.history.append(("assistant", response))
    st.chat_message("assistant").write(response)