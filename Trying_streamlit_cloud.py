import streamlit as st
import socket
#  FIX: All libraries imported safely at the top
import ollama
from groq import Groq

# Smart Function: Detects if the app is running on Streamlit Cloud or your PC
def is_running_on_cloud():
    try:
        # Streamlit Cloud URLs always contain 'streamlit.app'
        return "streamlit.app" in st.context.headers.get("Host", "")
    except:
        return False

st.title("JohnDoe's own ChatGPT")

# --- PROFILE 1: CLOUD MODE (Uses Google Gemini) ---
if is_running_on_cloud():
    st.caption("☁️ Cloud Mode: Powered by Groq Llama 3")
    
    # Read the secret key you saved in the Streamlit Cloud Dashboard
    if "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]
        
        def generate_response(questionToAsk):
            try:
                client = Groq(api_key=api_key)
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{'role': 'user', 'content': questionToAsk}]
                )
                st.info(response.choices.message.content)
            except Exception as e:
                st.error(f"Groq Cloud Error: {e}")
    else:
        st.error("Missing GROQ_API_KEY in Streamlit Secrets Dashboard.")

# --- PROFILE 2: LOCAL MODE (Uses your local Ollama) ---
else:
    st.caption("Local Mode: Powered by Ollama Llama 3.2:1b")
    
    def generate_response(questionToAsk):
        try:
            response = ollama.chat(
                model="llama3.2:1b", 
                messages=[{'role': 'user', 'content': questionToAsk}]
            )
            st.info(response['message']['content'])
        except Exception as e:
            st.error(f"Ollama Error. Is your local desktop app running? Details: {e}")

# --- UNIVERSAL USER INTERFACE ---
with st.form("my_form"):
    text = st.text_area(
        "Enter Text:",
        "Over here, ask a question and press the submit button",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
