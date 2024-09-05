import streamlit as st
from chatbot import *


# Function to handle the chat submission
def submit_data():
    if st.session_state.user_input:
        # Get the response from your function
        response = query_ollama(st.session_state.user_input)

        # Append user input and bot response to chat history
        st.session_state.chat_history.append(f"You: {st.session_state.user_input}")
        st.session_state.chat_history.append(f"Bot: {response}")
        
        # Clear input box after submitting
        st.session_state.user_input = ""

# Initialize chat history in session state if not already done
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Streamlit App title
st.title("Chatbot")

# Chat input field with callback to submit data when Enter is pressed
st.text_input("You:", key="user_input", on_change=submit_data)

# Display chat history
if st.session_state['chat_history']:
    for message in st.session_state['chat_history']:
        st.write(message)
