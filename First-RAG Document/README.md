# 📄 RAG Document Q&A — Ask Questions on Research Papers

A **Retrieval-Augmented Generation (RAG)** application that lets you ask questions about research PDF documents. Built with LangChain, FAISS vector database, HuggingFace embeddings, and Groq's LLaMA 3 for fast inference.

---

## 🚀 Project Overview

This project implements a complete RAG pipeline from scratch — document loading, chunking, embedding, vector storage, retrieval, and LLM-powered answering — all deployed as a Streamlit web app.

The knowledge base is built on two foundational AI research papers:
- **"Attention Is All You Need"** (Transformer paper)
- **"Large Language Models"** (LLM survey paper)

---

## 🎯 Features

- 📂 **PDF document loading** — Loads and processes multiple PDFs automatically
- ✂️ **Smart text chunking** — Splits documents into 1000-char chunks with 200-char overlap
- 🔢 **HuggingFace embeddings** — Uses `all-MiniLM-L6-v2` for semantic vector representations
- 🗄️ **FAISS vector store** — Local vector database for fast similarity search
- 🧠 **RetrievalQA chain** — Retrieves relevant context, then answers using LLaMA 3
- ⏱️ **Response time tracking** — Shows how long each query takes to process
- 📋 **Source document display** — Shows which document chunks were used to answer
- 💾 **Session state caching** — Embeddings are created once and reused (no re-embedding on every query)

---

## 🧠 RAG Architecture

```
PDF Documents (research_papers/ folder)
        ↓
PyPDFDirectoryLoader
        ↓
RecursiveCharacterTextSplitter
  [chunk_size=1000, chunk_overlap=200]
        ↓
HuggingFace Embeddings (all-MiniLM-L6-v2)
        ↓
FAISS Vector Store
        ↓
User Query → Similarity Search → Top-K Chunks (Context)
        ↓
RetrievalQA Chain
        ↓
ChatGroq LLM (LLaMA 3.3-70B)
        ↓
Answer + Source Documents (Streamlit UI)
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **LangChain** | RAG pipeline orchestration |
| **Groq API** | LLM inference (LLaMA 3.3-70B) |
| **FAISS** | Local vector similarity search |
| **HuggingFace Embeddings** | `all-MiniLM-L6-v2` sentence embeddings |
| **PyPDF** | PDF document loading |
| **Streamlit** | Web application UI |
| **python-dotenv** | Environment variable management |

---

## 📁 Project Structure

```
02-rag-document-qa/
├── app.py                  ← Main Streamlit RAG application
├── research_papers/        ← Place your PDF files here
│   ├── attention_paper.pdf
│   └── llm_paper.pdf
├── requirements.txt        ← Python dependencies
├── .env.example            ← Environment variable template
└── README.md
```

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/amritgupta0680/genai-portfolio.git
cd genai-portfolio/02-rag-document-qa
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**
```bash
cp .env.example .env
# Add your Groq API key inside .env
```

**4. Add your PDF files**
```bash
# Create the research_papers folder and add your PDFs
mkdir research_papers
# Copy your PDF files into research_papers/
```

**5. Run the app**
```bash
streamlit run app.py
```

**6. Click "Document Embedding" to build the vector store, then ask questions!**

---

## 🔑 Environment Variables

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

---

## 💡 Example Questions to Ask

- *"What is the attention mechanism and how does it work?"*
- *"What are the key components of the Transformer architecture?"*
- *"How are large language models trained?"*
- *"What is multi-head attention?"*

---

## 📌 What I Learned

- Building a complete RAG pipeline with LangChain
- Difference between embeddings and vector databases
- How FAISS stores and retrieves vectors by similarity
- Using `session_state` in Streamlit to cache expensive operations
- Displaying source document chunks for answer transparency

---

## 👤 Author

**Amrit Gupta** — B.E. in Artificial Intelligence & Data Science

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/amrit-gupta-1162b232a/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/amritgupta0680)

---

⭐ Part of the [GenAI Portfolio](../README.md) — a collection of end-to-end Generative AI projects.
