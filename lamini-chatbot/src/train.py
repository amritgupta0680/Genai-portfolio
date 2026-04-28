from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model
from datasets import Dataset
import json

model_name = "distilgpt2"

# Load tokenizer + model
tokenizer = AutoTokenizer.from_pretrained(model_name)

# FIX 1: add padding token
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name)

# IMPORTANT: set pad token id in model config
model.config.pad_token_id = tokenizer.pad_token_id


# Load dataset
with open("../data/dataset.json") as f:
    data = json.load(f)

# Format dataset
texts = [f"User: {d['input']}\nBot: {d['output']}" for d in data]
dataset = Dataset.from_dict({"text": texts})


# FIX 2: add labels for training
def tokenize(example):
    tokens = tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=128   # keep small for CPU
    )

    tokens["labels"] = tokens["input_ids"].copy()
    return tokens


dataset = dataset.map(tokenize, remove_columns=["text"])


# LoRA config
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["c_attn"],
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM"   # FIX 3: important for stability
)

model = get_peft_model(model, lora_config)


# Training args (CPU-friendly)
training_args = TrainingArguments(
    output_dir="../model",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    logging_steps=5,
    save_strategy="no",
    fp16=False   # IMPORTANT: CPU users
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)


print("Training started...\n")
trainer.train()


# Save model
model.save_pretrained("../model")
tokenizer.save_pretrained("../model")

print("\n✅ Training completed!")