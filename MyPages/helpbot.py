import streamlit as st
import ollama

def show_helpbot():
    st.title("🤖 AI HelpBot")

    # Store chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show old messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    prompt = st.chat_input("Ask something...")

    if prompt:
        # Save user message
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        # Get response from Ollama
        response = ollama.chat(
            model="llama3.2",
            messages=st.session_state.messages
        )

        reply = response["message"]["content"]

        # Save bot reply
        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.markdown(reply)