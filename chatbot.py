import google.generativeai as gn
import streamlit as st

# Page setup
st.set_page_config(page_title="Chat MAR⚙️1316", page_icon="🤖", layout="centered")

# 🧼 Clean, modern CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f9fafb;
        }
        .chat-message {
            padding: 12px 18px;
            border-radius: 18px;
            margin: 8px 0;
            max-width: 75%;
            font-size: 16px;
            line-height: 1.5;
        }
        .user-msg {
            background-color: black;
            color: white;
            margin-left: auto;
            text-align: right;
        }
        .bot-msg {
            background-color: #e5e7eb;
            color: #111827;
            margin-right: auto;
            text-align: left;
        }
        .stChatInput input {
            background-color: #f3f4f6;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: red;'>🤖 Chat MAR ⚙️ 1316</h1>", unsafe_allow_html=True)

# Gemini API configuration
api = 'AIzaSyD2pCCj2iLCTmTfQF68NQ6QPq6sbR8UyRs'
if api:
    gn.configure(api_key=api)
else:
    st.error("❌ API key is missing or invalid.")

# Text generation function
def generate_text(text):
    model = gn.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content(text, stream=True)
    return ''.join([chunk.text for chunk in response])


# Chat memory
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Render previous chat
for message in st.session_state.messages:
    role_class = 'user-msg' if message['role'] == 'user' else 'bot-msg'
    st.markdown(f"<div class='chat-message {role_class}'>{message['content']}</div>", unsafe_allow_html=True)

# Input field
user_input = st.chat_input("💬 Type your message...")

# Handle user input
if user_input:
    st.markdown(f"<div class='chat-message user-msg'>{user_input}</div>", unsafe_allow_html=True)
    st.session_state.messages.append({'role': 'user', 'content': user_input})

    with st.spinner("🤖 Gemini is thinking..."):
        bot_response = generate_text(user_input)
        st.markdown(f"<div class='chat-message bot-msg'>{bot_response}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({'role': 'assistant', 'content': bot_response})
