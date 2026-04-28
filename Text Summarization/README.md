# 📝 YouTube & Website Text Summarizer

An AI-powered **text summarization app** that generates concise 300-word summaries of any YouTube video or website URL. Available in two versions — one powered by **Groq (LLaMA 3)** and another by **HuggingFace (Zephyr 7B)** — demonstrating how to swap LLM backends in LangChain.

---

## 🚀 Project Overview

This project demonstrates LangChain's **summarization chains** applied to real-world content sources. It handles the full pipeline: fetching content from a URL, splitting it into manageable chunks, and summarizing using an LLM.

A key feature is the **smart fallback logic** — if a YouTube video has no transcript available, the app automatically falls back to web scraping the page content instead of failing.

---

## 🎯 Features

- 🎬 **YouTube video summarization** — Extracts transcript and summarizes in 300 words
- 🌐 **Website summarization** — Scrapes and summarizes any webpage
- 🔁 **Smart fallback** — If YouTube transcript unavailable, falls back to URL scraping automatically
- 🤖 **Dual LLM support** — Choose between Groq (fast) or HuggingFace (open source)
- ✅ **Input validation** — Validates URLs before processing
- ❌ **Empty content detection** — Handles cases where no content can be extracted

---

## 📂 Two Versions

### `app.py` — Groq Version (Recommended)
- Uses **LLaMA 3.3-70B** via Groq API
- Faster inference
- Requires Groq API key (free at console.groq.com)

### `huggingface_app.py` — HuggingFace Version
- Uses **Zephyr 7B Beta** via HuggingFace Inference API
- Fully open-source model
- Requires HuggingFace API token

---

## 🧠 Architecture

```
User Input (URL)
        ↓
URL Validation (validators library)
        ↓
Content Loading
  ├── YouTube URL? → YoutubeLoader (transcript)
  │       ↓ (if transcript fails)
  └── Fallback → UnstructuredURLLoader (web scrape)
        ↓
RecursiveCharacterTextSplitter
  [chunk_size=2000, chunk_overlap=200]
        ↓
Summarization Chain (stuff chain_type)
  PromptTemplate: "Summarize in 300 words"
        ↓
Groq LLM (LLaMA 3.3-70B)
  OR
HuggingFace (Zephyr 7B Beta)
        ↓
Summary Output (Streamlit UI)
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **LangChain** | Summarization chain orchestration |
| **Groq API** | Fast LLM inference (app.py) |
| **HuggingFace Endpoint** | Open-source LLM (huggingface_app.py) |
| **LLaMA 3.3-70B** | LLM for Groq version |
| **Zephyr 7B Beta** | LLM for HuggingFace version |
| **YoutubeLoader** | YouTube transcript extraction |
| **UnstructuredURLLoader** | Website content scraping |
| **validators** | URL validation |
| **Streamlit** | Web application UI |

---

## 📁 Project Structure

```
04-text-summarizer/
├── app.py                  ← Groq version (LLaMA 3)
├── huggingface_app.py      ← HuggingFace version (Zephyr 7B)
├── requirements.txt        ← Python dependencies
├── .env.example            ← Environment variable template
└── README.md
```

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/amritgupta0680/genai-portfolio.git
cd genai-portfolio/04-text-summarizer
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run Groq version**
```bash
streamlit run app.py
# Enter your Groq API key in the sidebar
```

**OR run HuggingFace version**
```bash
streamlit run huggingface_app.py
# Enter your HuggingFace API token in the sidebar
```

**4. Paste any YouTube or website URL and click Summarize!**

---

## 💡 Example URLs to Try

- Any YouTube tutorial or lecture video
- A news article from BBC, TechCrunch, etc.
- A research blog post
- A Wikipedia article

---

## 📌 What I Learned

- LangChain's `load_summarize_chain` with different chain types (`stuff`, `map_reduce`)
- Loading content from YouTube and websites using LangChain document loaders
- Building fallback logic for robust content fetching
- How to swap LLM backends in LangChain (Groq vs HuggingFace)
- Handling edge cases: empty content, failed transcripts, invalid URLs

---

## 👤 Author

**Amrit Gupta** — B.E. in Artificial Intelligence & Data Science

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/amrit-gupta-1162b232a/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/amritgupta0680)

---

⭐ Part of the [GenAI Portfolio](../README.md) — a collection of end-to-end Generative AI projects.
