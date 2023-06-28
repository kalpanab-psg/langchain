import os
from constants import openai_key
os.environ['OPENAI_API_KEY']=openai_key



import streamlit as st
from langchain.llms import OpenAI

st.title('🦜️🔗 LangChain')
prompt=st.text_input('enter your prompt')

llms=OpenAI(temperature=0.9)

if prompt:
    response=llms(prompt)
    st.write(response)
