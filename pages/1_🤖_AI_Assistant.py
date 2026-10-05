import streamlit as st

from ollama_client import ask_ai
from safety import check_emergency


st.set_page_config(
    page_title="AI Healthcare Assistant",
    page_icon="🤖"
)


st.title("🤖 AI Healthcare Assistant")

st.write(
    "Ask general healthcare questions and get "
    "assistance from our local AI."
)

st.caption(
    "⚠️ This AI provides general information only. "
    "It does not diagnose diseases or replace a doctor."
)


# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
question = st.chat_input(
    "Type your healthcare question..."
)


if question:

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })


    # Display user message
    with st.chat_message("user"):
        st.write(question)


    # Check for possible emergency
    if check_emergency(question):

        answer = """
🚨 **Please seek immediate medical attention.**

Your message may describe a potentially serious
medical situation.

This AI assistant cannot safely evaluate or manage
a medical emergency.

Please contact your local emergency medical service
or go to the nearest emergency department.
"""

    else:

        # Ask Ollama
        with st.spinner("AI is thinking..."):

            answer = ask_ai(question)


    # Display AI response
    with st.chat_message("assistant"):

        st.write(answer)


    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
