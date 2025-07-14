from .env import load_.env
load_.env() 
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-2.0-flash")

def my_output(query):
    response=model.generate_content(query)
    return response.txt

st.set_page_config(page_title="chat_bot")
st.header("chat_bot")
input=st.text_input("Input",key="input")
submit=st.button("Ask your query")

if submit:
    response=my_output(input)
    st.subheader("Response :-")
    st.write(response)
