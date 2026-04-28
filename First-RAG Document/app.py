import streamlit as st
import os
import time

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# -----------------------------
# Load ENV
# -----------------------------
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# -----------------------------
# LLM
# -----------------------------
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile"
)

# -----------------------------
# Function: Create Vector DB
# -----------------------------
def create_vector_embedding():

    if "vectors" not in st.session_state:

        # ✅ FIX: stable embeddings (NO META ERROR)
        st.session_state.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )

        # Load PDFs
        st.session_state.loader = PyPDFDirectoryLoader("research_papers")
        st.session_state.docs = st.session_state.loader.load()

        # Split
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        st.session_state.final_documents = st.session_state.text_splitter.split_documents(
            st.session_state.docs[:50]
        )

        # Vector store
        st.session_state.vectors = FAISS.from_documents(
            st.session_state.final_documents,
            st.session_state.embeddings
        )

# -----------------------------
# UI
# -----------------------------
st.title("📄 RAG Document Q&A with Groq + LLaMA3")

user_prompt = st.text_input("Enter your query from the research paper")

if st.button("Document Embedding"):
    create_vector_embedding()
    st.success("Vector Database is ready ✅")

# -----------------------------
# QA
# -----------------------------
if user_prompt:

    if "vectors" not in st.session_state:
        st.warning("⚠️ Please click 'Document Embedding' first")
    else:
        retriever = st.session_state.vectors.as_retriever()

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True
        )

        start = time.process_time()
        response = qa_chain({"query": user_prompt})
        end = time.process_time()

        st.write("### 🧠 Answer:")
        st.write(response["result"])

        st.write(f"⏱️ Response time: {end - start:.2f} sec")

        # Show context
        with st.expander("📄 Document Similarity Search"):
            for doc in response["source_documents"]:
                st.write(doc.page_content)
                st.write("------------------------")