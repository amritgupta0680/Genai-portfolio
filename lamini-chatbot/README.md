# 🧠 Lamini Fine-Tuned Chatbot — LoRA Fine-Tuning on Custom Data

A complete **LLM fine-tuning project** that trains a custom LoRA adapter on `distilgpt2` using a personal dataset, then deploys a Streamlit app that compares **Base Model vs Fine-Tuned Model** responses side by side.

---

## 🚀 Project Overview

This project goes beyond prompt engineering — it demonstrates the full **LLM fine-tuning lifecycle**:

1. Prepare a custom conversational dataset
2. Configure LoRA (Low-Rank Adaptation) for parameter-efficient fine-tuning
3. Train on CPU using HuggingFace `Trainer` API
4. Save the fine-tuned LoRA adapter
5. Deploy a comparison app showing Base vs Fine-Tuned responses

This is a practical implementation of **PEFT (Parameter-Efficient Fine-Tuning)** — a technique used in production to adapt large models to specific domains without retraining the entire model.

---

## 🎯 Features

- 📊 **Custom dataset training** — Fine-tunes on your own `dataset.json` conversation pairs
- 🔧 **LoRA fine-tuning** — Trains only a small adapter (not the full model weights)
- 💻 **CPU-compatible** — Training runs on CPU (no GPU required, fp16 disabled)
- 🤖 **Side-by-side comparison** — Two-column Streamlit UI showing Base vs Fine-Tuned output
- 💾 **Adapter saving** — Saves LoRA adapter separately (efficient storage)
- 🎯 **Response extraction** — Parses `Bot:` response cleanly from generated text

---

## 🧠 How LoRA Fine-Tuning Works

```
Base Model (distilgpt2 — frozen weights)
        +
LoRA Adapter (small trainable matrices)
  Config:
    r = 8                    (rank — controls adapter size)
    lora_alpha = 16          (scaling factor)
    target_modules = c_attn  (attention layers to adapt)
    lora_dropout = 0.1
    task_type = CAUSAL_LM
        ↓
Training on custom dataset.json
  Format: "User: {input}\nBot: {output}"
  Epochs: 3
  Batch size: 2
        ↓
Fine-Tuned LoRA Adapter saved to ../model/
        ↓
Comparison App:
  Base Model (distilgpt2)  |  Fine-Tuned Model (distilgpt2 + LoRA)
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **HuggingFace Transformers** | Base model loading, tokenizer, Trainer |
| **PEFT** | LoRA configuration and adapter wrapping |
| **distilgpt2** | Base causal language model |
| **datasets (HuggingFace)** | Dataset creation and tokenization |
| **Streamlit** | Web app for Base vs Fine-Tuned comparison |
| **python-dotenv** | Environment variable management |

---

## 📁 Project Structure

```
05-lamini-finetuned-chatbot/
├── src/
│   ├── train.py            ← LoRA fine-tuning script
│   ├── chat.py             ← CLI chat interface
│   └── app.py              ← Streamlit comparison app
├── data/
│   └── dataset.json        ← Custom training conversations
├── model/                  ← Saved LoRA adapter (generated after training)
│   ├── adapter_model.safetensors
│   └── adapter_config.json
├── requirements.txt        ← Python dependencies
├── .env.example            ← Environment variable template
└── README.md
```

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/amritgupta0680/genai-portfolio.git
cd genai-portfolio/05-lamini-finetuned-chatbot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. (Optional) Add your own training data**

Edit `data/dataset.json` — format:
```json
[
  {"input": "Hello, how are you?", "output": "I'm doing great, thanks for asking!"},
  {"input": "What can you help me with?", "output": "I can answer questions and have conversations with you."}
]
```

**4. Train the model**
```bash
cd src
python train.py
# Training takes ~5-10 minutes on CPU
# Model saved to ../model/
```

**5. Run the comparison app**
```bash
streamlit run src/app.py
```

**6. Ask questions and compare Base vs Fine-Tuned responses!**

---

## 📊 Training Configuration

| Parameter | Value |
|-----------|-------|
| Base model | distilgpt2 |
| LoRA rank (r) | 8 |
| LoRA alpha | 16 |
| Target modules | c_attn (attention) |
| Dropout | 0.1 |
| Epochs | 3 |
| Batch size | 2 |
| Max sequence length | 128 tokens |
| Hardware | CPU (fp16=False) |

---

## 📌 What I Learned

- How LoRA (Low-Rank Adaptation) works mathematically and practically
- The difference between full fine-tuning and PEFT
- HuggingFace `Trainer` API — TrainingArguments, dataset tokenization, label setup
- Why `labels = input_ids` is needed for causal language model training
- How to load and merge a LoRA adapter with the base model using `PeftModel`
- Building a side-by-side comparison UI in Streamlit

---

## 🔮 Future Improvements

- Train on a larger custom dataset for better responses
- Add quantization (QLoRA) for even more efficient training
- Deploy on HuggingFace Spaces
- Experiment with larger base models (GPT-2 Medium, LLaMA)

---

## 👤 Author

**Amrit Gupta** — B.E. in Artificial Intelligence & Data Science

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/amrit-gupta-1162b232a/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/amritgupta0680)

---

⭐ Part of the [GenAI Portfolio](../README.md) — a collection of end-to-end Generative AI projects.
