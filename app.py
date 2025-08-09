import streamlit as st
import time, random
from chatbot import get_response

# Streamlit page config
st.set_page_config(page_title="Mixtral AI Chatbot", page_icon="🤖", layout="centered")

# Sidebar controls
with st.sidebar:
    st.title("⚙️ Settings")
    tone = st.radio("Select Reply Tone:", ["Friendly", "Professional"])
    theme = st.radio("Theme Mode:", ["Light", "Dark"])
    st.markdown("---")
    st.markdown("**Quick Questions:**")
    if st.button("🌍 What is AI?"):
        st.session_state.quick_question = "What is AI?"
    if st.button("🚀 How to learn Python?"):
        st.session_state.quick_question = "How to learn Python?"
    if st.button("💡 Tell me a fact"):
        st.session_state.quick_question = "Tell me an interesting fact"

# Title
st.title("💬 Mixtral AI Chatbot")
st.markdown("Ask me anything!")

# Handle quick question click
if "quick_question" in st.session_state:
    default_text = st.session_state.quick_question
    del st.session_state.quick_question
else:
    default_text = ""

# Input field
user_input = st.text_input("Your Message:", value=default_text, placeholder="Type here...")

# Character limit warning
if len(user_input) > 200:
    st.warning("⚠️ Your message is too long! Consider making it shorter.")

# Response
if user_input:
    with st.spinner("Thinking..."):
        bot_reply = get_response(user_input, tone)

    # Typing effect
    placeholder = st.empty()
    full_reply = ""
    for char in bot_reply:
        full_reply += char
        time.sleep(0.01)
        placeholder.markdown(f"🤖 **Bot:** {full_reply}")

    # Add random emoji reaction
    emoji = random.choice(["😊", "👍", "🤔", "💡", "🎯"])
    st.markdown(f"**Bot Reaction:** {emoji}")

    # Clear input after response
    st.session_state["user_input"] = ""
