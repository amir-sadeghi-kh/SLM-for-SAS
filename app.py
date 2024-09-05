from chatbot import *
import streamlit as st

# Placeholder function for returning chatbot responses
def get_response(query):
    return f"Response to: {query}"

# Function to handle the chat submission
def submit_data():
    if st.session_state.user_input:
        # Get the response from your function
        response = query_ollama(st.session_state.user_input)

        # Append user input and bot response to chat history
        st.session_state.chat_history.append({"message": st.session_state.user_input, "is_user": True})
        st.session_state.chat_history.append({"message": response, "is_user": False})
        
        # Clear input box after submitting
        st.session_state.user_input = ""

# Initialize chat history in session state if not already done
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Streamlit App title
st.title("Conversational Chatbot")

# Define custom CSS for chat bubble styling
st.markdown("""
    <style>
    .user-bubble {
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 60%;
        text-align: right;
        float: right;
    }
    .bot-bubble {
        background-color: #F1F0F0;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 60%;
        text-align: left;
        float: left;
    }
    .clearfix {
        clear: both;
    }
    </style>
    """, unsafe_allow_html=True)

# Chat input field with callback to submit data when Enter is pressed
st.text_input("You:", key="user_input", on_change=submit_data)

# Display chat history with styled bubbles
for chat in st.session_state['chat_history']:
    if chat['is_user']:
        st.markdown(f'<div class="user-bubble">{chat["message"]}</div><div class="clearfix"></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">{chat["message"]}</div><div class="clearfix"></div>', unsafe_allow_html=True)
