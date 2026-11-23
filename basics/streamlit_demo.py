
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.globals import set_debug

set_debug(True)


llm=ChatOpenAI(model="gpt-4o",)

st.title("Ask Anything")

question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)