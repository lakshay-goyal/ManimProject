import streamlit as st
from app.chatbot import chatbot_response


# Set up the page
st.set_page_config(page_title="Simple Chatbot UI", layout="centered")
st.title("💬 Simple Chatbot")

# Initialize chat history in session state (used to store messages)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show previous chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["sender"]):
        st.markdown(message["text"])

# Input field for the user to type a message
user_message = st.chat_input("Type your message...")

# If the user sends a message
if user_message:
    # Show user's message
    st.chat_message("user").markdown(user_message)
    # Save user's message to history
    st.session_state.chat_history.append({"sender": "user", "text": user_message})

    if user_message:
        response = st.write_stream(chatbot_response(user_message))
        st.chat_message("assistant").markdown(response)
        st.session_state.chat_history.append({"sender": "assistant", "text": response})
