# 🧮 MathsGPT — AI Math Problem Solver Agent

An intelligent **AI agent** that solves math problems, logic questions, and reasoning tasks step-by-step. Built with LangChain's ReAct agent framework, it uses three specialized tools — a Calculator, Wikipedia search, and a Reasoning chain — and displays its entire thought process live in the UI.

---

## 🚀 Project Overview

This project goes beyond a simple chatbot — it implements a **multi-tool agentic system** where the AI decides which tools to use, in what order, and how to combine their results to arrive at the final answer.

The agent follows the **ReAct (Reasoning + Acting)** pattern:
> Think → Choose a tool → Observe the result → Think again → Final answer

---

## 🎯 Features

- 🔢 **Calculator tool** — Solves mathematical expressions using `LLMMathChain`
- 🌐 **Wikipedia tool** — Searches the web for facts needed to solve problems
- 💡 **Reasoning tool** — Handles logic-based questions with step-by-step explanation
- 🧠 **ReAct agent** — Autonomously decides which tool to use for each question
- 📡 **Live thought process** — `StreamlitCallbackHandler` shows the agent's reasoning in real time
- 💬 **Conversation history** — Maintains chat history across multiple questions
- ⚠️ **Error handling** — Gracefully handles parsing errors with `handle_parsing_errors=True`

---

## 🧠 Agent Architecture

```
User Question (Streamlit)
        ↓
ZERO_SHOT_REACT_DESCRIPTION Agent
        ↓
    [Think: Which tool do I need?]
        ↓
  ┌─────────────────────────────────┐
  │         Available Tools         │
  │  🔢 Calculator (LLMMathChain)   │
  │  🌐 Wikipedia Search            │
  │  💡 Reasoning Chain (LLMChain)  │
  └─────────────────────────────────┘
        ↓
    [Observe result]
        ↓
    [Repeat if needed]
        ↓
Final Answer → Streamlit UI
(with live thought stream via StreamlitCallbackHandler)
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **LangChain Agents** | ReAct agent orchestration |
| **Groq API** | LLM inference (LLaMA 3.1-8B) |
| **LLMMathChain** | Mathematical expression solver |
| **WikipediaAPIWrapper** | Real-time Wikipedia search |
| **LLMChain** | Custom reasoning chain |
| **StreamlitCallbackHandler** | Live agent thought display |
| **Streamlit** | Web application UI |

---

## 📁 Project Structure

```
03-mathsgpt-agent/
├── app.py              ← Main Streamlit agent application
├── requirements.txt    ← Python dependencies
├── .env.example        ← Environment variable template
└── README.md
```

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/amritgupta0680/genai-portfolio.git
cd genai-portfolio/03-mathsgpt-agent
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

**4. Enter your Groq API key in the sidebar and ask a math question!**

> 💡 The Groq API key is entered directly in the sidebar at runtime — free to get at [console.groq.com](https://console.groq.com)

---

## 💡 Example Questions to Try

- *"I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries (25 berries each). How many fruits total?"*
- *"What is the square root of 144 plus the cube of 5?"*
- *"Who invented calculus and what year was it?"*
- *"If a train travels 120 km in 1.5 hours, what is its speed in m/s?"*

---

## 📌 What I Learned

- How LangChain agents work — the ReAct (Reasoning + Acting) loop
- Difference between chains and agents
- How to define custom tools and register them with an agent
- Using `StreamlitCallbackHandler` to expose agent thinking in real time
- Managing conversation history in `session_state`

---

## 👤 Author

**Amrit Gupta** — B.E. in Artificial Intelligence & Data Science

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/amrit-gupta-1162b232a/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/amritgupta0680)

---

⭐ Part of the [GenAI Portfolio](../README.md) — a collection of end-to-end Generative AI projects.
