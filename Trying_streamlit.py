import streamlit as st
import ollama
desiredModel = "llama3.2:1b"
st.title("Krishna's own ChatGPT")

def generate_response(questionToAsk):
    response=ollama.chat(model=desiredModel, messages=[
        {
            'role':'user',
            'content': questionToAsk,
        },
        ])
    st.info(response['message'] ['content'])

with st.form("my_form"):
    text=st.text_area(
        "Enter Text:",
        "Over here, ask a question and press the submit button",
    )
    submitted=st.form_submit_button("Submit")
    if submitted:
        generate_response(text)

