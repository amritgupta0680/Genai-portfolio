import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# Paths
model_path = "../model"
base_model_name = "distilgpt2"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)
tokenizer.pad_token = tokenizer.eos_token

# 🔹 Load BASE model (normal)
base_model = AutoModelForCausalLM.from_pretrained(base_model_name)

# 🔹 Load FINE-TUNED model (LoRA)
finetuned_model = PeftModel.from_pretrained(
    AutoModelForCausalLM.from_pretrained(base_model_name),
    model_path
)

# Streamlit UI
st.title("🤖 Chatbot Comparison: Base vs Fine-Tuned")

st.write("Compare responses between:")
st.write("- Base Model (distilgpt2)")
st.write("- Fine-tuned Model (your trained chatbot)")

user_input = st.text_input("Enter your question:")

def generate_response(model, prompt):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True)

    outputs = model.generate(
        **inputs,
        max_length=100,
        do_sample=True,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if "Bot:" in response:
        response = response.split("Bot:")[-1].strip()

    return response


if user_input:
    prompt = f"User: {user_input}\nBot:"

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🤖 Base Model Response")
        base_response = generate_response(base_model, prompt)
        st.write(base_response)

    with col2:
        st.subheader("🧠 Fine-Tuned Model Response")
        finetuned_response = generate_response(finetuned_model, prompt)
        st.write(finetuned_response)