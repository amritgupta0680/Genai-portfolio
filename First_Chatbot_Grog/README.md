# 🤖 Q&A Chatbot with Groq API

A conversational **Q&A chatbot** built with LangChain and Groq API, featuring multiple LLM model selection, adjustable parameters, and LangSmith tracing for observability.

---

## 🚀 Project Overview

This project demonstrates building a production-ready chatbot using the **LCEL (LangChain Expression Language)** pipeline pattern:

```
User Question → Prompt Template → Groq LLM → Output Parser → Response
```

The app gives users full control over the model, temperature, and token length directly from the sidebar — making it easy to experiment and compare outputs.

---

## 🎯 Features

- 🧠 **Multi-model support** — Switch between LLaMA 3.3 70B, LLaMA 3.1 8B, and Mixtral 8x7B
- 🎛️ **Adjustable parameters** — Control temperature (creativity) and max tokens (response length)
- 🔍 **LangSmith tracing** — Full observability of chain execution in LangSmith dashboard
- 🔒 **Secure API key input** — Key entered at runtime via sidebar, never hardcoded
- ⚡ **LCEL chain** — Uses modern LangChain Expression Language for clean pipeline composition

---

## 🧠 Architecture

```
User Input (Streamlit)
        ↓
ChatPromptTemplate
  [System: "You are a helpful assistant"]
  [Human: "{question}"]
        ↓
ChatGroq LLM
  (LLaMA 3.3-70B / LLaMA 3.1-8B / Mixtral-8x7B)
        ↓
StrOutputParser
        ↓
Response (Streamlit UI)
        ↓
LangSmith Tracing (background)
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **LangChain** | Chain composition using LCEL |
| **Groq API** | Fast LLM inference (LPU hardware) |
| **LLaMA 3.3 70B / 3.1 8B** | Language models |
| **Mixtral 8x7B** | Alternative MoE model |
| **Streamlit** | Web application UI |
| **LangSmith** | Chain tracing and observability |
| **python-dotenv** | Environment variable management |

---

## 📁 Project Structure

```
01-chatbot-groq/
├── app.py              ← Main Streamlit application
├── requirements.txt    ← Python dependencies
├── .env.example        ← Environment variable template
└── README.md
```

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/amritgupta0680/genai-portfolio.git
cd genai-portfolio/01-chatbot-groq
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**
```bash
cp .env.example .env
# Add your LangSmith API key inside .env
```

**4. Get your Groq API key**
- Sign up at [console.groq.com](https://console.groq.com)
- Create a free API key

**5. Run the app**
```bash
streamlit run app.py
```

**6. Enter your Groq API key in the sidebar and start chatting!**

---

## 🔑 Environment Variables

```env
LANGCHAIN_API_KEY=your_langsmith_api_key_here
```

> 💡 The Groq API key is entered directly in the sidebar at runtime — no need to add it to `.env`.

---

## 📌 What I Learned

- Building LangChain chains using the modern LCEL `|` pipeline syntax
- Integrating Groq API for ultra-fast LLM inference
- Setting up LangSmith for chain tracing and debugging
- Handling API keys securely in Streamlit apps

---

## 👤 Author

**Amrit Gupta** — B.E. in Artificial Intelligence & Data Science

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/amrit-gupta-1162b232a/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/amritgupta0680)

---

⭐ Part of the [GenAI Portfolio](../README.md) — a collection of end-to-end Generative AI projects.
