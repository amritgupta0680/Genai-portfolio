import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

## LangSmith Tracking
os.environ["LANGCHAIN_API_KEY2"] = os.getenv("LANGCHAIN_API_KEY2")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With GROQ"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key, model, temperature, max_tokens):

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name=model,
        temperature=temperature,
        max_tokens=max_tokens
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    answer = chain.invoke({'question': question})
    return answer


## Title
st.title("Enhanced Q&A Chatbot With GROQ")

## Sidebar
st.sidebar.title("Settings")

api_key = st.sidebar.text_input("Enter your GROQ API Key:", type="password")

## Groq Models
model = st.sidebar.selectbox(
    "Select Groq Model",
    ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    min_value=50,
    max_value=300,
    value=150
)

## User Input
st.write("Go ahead and ask any question")

user_input = st.text_input("You:")

if user_input and api_key:
    response = generate_response(
        user_input,
        api_key,
        model,
        temperature,
        max_tokens
    )
    st.write(response)

elif user_input:
    st.warning("Please enter the GROQ API Key in the sidebar")

else:
    st.write("Please provide the user input")