from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

model_path = "../model"
base_model_name = "distilgpt2"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)
tokenizer.pad_token = tokenizer.eos_token

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(base_model_name)

# 🔥 LOAD LORA WEIGHTS (IMPORTANT FIX)
model = PeftModel.from_pretrained(base_model, model_path)

print("Chatbot ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    prompt = f"User: {user_input}\nBot:"

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

    print("Bot:", response)