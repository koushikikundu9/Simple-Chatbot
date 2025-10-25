import os
import streamlit as st
from langchain_classic.schema import HumanMessage, AIMessage
from main import chat_with_gemini

# --- Page setup ---
st.set_page_config(page_title="AuraByte", page_icon="🤖", layout="centered")
os.environ['GEMAI_API_KEY']=st.secrets['GEMAI_API_KEY']
# --- Custom CSS ---
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("style.css") 
# --- Fixed header ---
st.markdown("<div>",unsafe_allow_html=True)
st.markdown("""
<div class="fixed-header">
    <h2>AuraByte 🤖</h2>
    <p>Chat with your personal Gemini-powered assistant:</p>
</div>
""",unsafe_allow_html=True)
st.markdown('<div class="spacer"></div>',unsafe_allow_html=True)
# --- Scrollable conversation area ---
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.write("✍️ Send a Message")
else:
    st.markdown("💬 Conversations")
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.markdown(f"<div class='user-bubble'>{msg.content}</div>", unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f"<div class='bot-bubble'>{msg.content}</div>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")
st.markdown("</div>",unsafe_allow_html=True)

# --- Fixed input box ---
st.markdown('<div class="fixed-input">', unsafe_allow_html=True)
user_input = st.chat_input("🪶Type your message here...")
st.markdown('</div>', unsafe_allow_html=True)
# --- Handle input ---
if user_input:
    with st.spinner("Thinking..."):
        try:
            st.markdown(f"<div class='user-bubble'>{user_input}</div>", unsafe_allow_html=True)
            response = chat_with_gemini(st.session_state.chat_history, user_input)
        except Exception as e:
            response = f"⚠️ Error: {e}"
    st.rerun()

# --- Sidebar ---
st.sidebar.button("🧹 Clear Chat", on_click=lambda: st.session_state.clear())






