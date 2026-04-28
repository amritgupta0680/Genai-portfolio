# 🤖 Generative AI Portfolio — Amrit Gupta

An end-to-end collection of **Generative AI projects** built while learning the complete GenAI stack — from LangChain fundamentals to LLM fine-tuning. Each project is a working application covering a different area of the GenAI ecosystem.

---

## 🚀 About This Repository

This portfolio was built during a structured GenAI learning journey covering:

- **LangChain** — chains, agents, tools, memory, retrievers
- **RAG (Retrieval-Augmented Generation)** — vector databases, embeddings, document loaders
- **LLM APIs** — Groq (LLaMA 3), HuggingFace (Zephyr 7B), OpenAI
- **LLM Fine-Tuning** — LoRA, PEFT, HuggingFace Transformers
- **Deployment** — Streamlit web apps

---

## 📁 Projects

| # | Project | Description | Key Tech |
|---|---------|-------------|----------|
| 01 | [🤖 Chatbot with Groq](./01-chatbot-groq/) | Q&A chatbot with multiple LLM model selection and LangSmith tracing | LangChain, Groq, LLaMA 3, Streamlit |
| 02 | [📄 RAG Document Q&A](./02-rag-document-qa/) | Ask questions on research PDFs using RAG pipeline | FAISS, HuggingFace Embeddings, Groq, PyPDF |
| 03 | [🧮 MathsGPT Agent](./03-mathsgpt-agent/) | AI agent that solves math problems using Calculator + Wikipedia tools | LangChain Agents, ReAct, LLMMathChain |
| 04 | [📝 Text Summarizer](./04-text-summarizer/) | Summarize YouTube videos and websites using two LLM backends | Groq, HuggingFace Zephyr, YoutubeLoader |
| 05 | [🧠 Lamini Fine-Tuned Chatbot](./05-lamini-finetuned-chatbot/) | Fine-tuned chatbot using LoRA on custom dataset with Base vs Fine-tuned comparison | LoRA, PEFT, distilgpt2, HuggingFace Transformers |

---

## 🛠️ Tech Stack

- **Languages:** Python
- **Frameworks:** LangChain, Streamlit, HuggingFace Transformers, PEFT
- **LLM APIs:** Groq (LLaMA 3.1, LLaMA 3.3, Mixtral), HuggingFace (Zephyr 7B)
- **Vector Databases:** FAISS
- **Embeddings:** HuggingFace all-MiniLM-L6-v2
- **Fine-tuning:** LoRA (Low-Rank Adaptation), PEFT
- **Tracking:** LangSmith

---

## 📂 Repository Structure

```
genai-portfolio/
│
├── README.md                        ← You are here
│
├── 01-chatbot-groq/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── 02-rag-document-qa/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── 03-mathsgpt-agent/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── 04-text-summarizer/
│   ├── app.py                       ← Groq version
│   ├── huggingface_app.py           ← HuggingFace version
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
└── 05-lamini-finetuned-chatbot/
    ├── src/
    │   ├── train.py
    │   ├── chat.py
    │   └── app.py
    ├── data/
    │   └── dataset.json
    ├── requirements.txt
    ├── .env.example
    └── README.md
```

---

## ⚙️ Getting Started

Each project has its own `README.md` with full setup instructions. General steps:

```bash
# Clone the repo
git clone https://github.com/amritgupta0680/genai-portfolio.git
cd genai-portfolio

# Navigate to any project
cd 01-chatbot-groq

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 👤 Author

**Amrit Gupta**
B.E. in Artificial Intelligence & Data Science

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/amrit-gupta-1162b232a/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/amritgupta0680)

---

⭐ If you find these projects useful, feel free to star the repository!
