#!/usr/bin/env python3
"""
Fine-tune LLaMA 3 for CodePilot
Uses QLoRA for efficient training on consumer hardware
"""

import json
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import Dataset
import os

print("🚀 CodePilot Fine-Tuning Script")
print("=" * 60)

# Configuration
MODEL_NAME = "meta-llama/Meta-Llama-3-8B"  # or use local path
OUTPUT_DIR = "./models/codepilot-custom"
DATA_FILE = "./data/training_data.json"

# Training parameters
BATCH_SIZE = 4
LEARNING_RATE = 2e-4
NUM_EPOCHS = 3
MAX_LENGTH = 512

print(f"📁 Loading training data from {DATA_FILE}")

# Load training data
with open(DATA_FILE, 'r') as f:
    data = json.load(f)

print(f"✅ Loaded {len(data)} training examples")

# Format data for training
def format_prompt(example):
    instruction = example['instruction']
    input_text = example.get('input', '')
    output = example['output']
    
    if input_text:
        prompt = f"### Instruction:\n{instruction}\n\n### Input:\n{input_text}\n\n### Response:\n{output}"
    else:
        prompt = f"### Instruction:\n{instruction}\n\n### Response:\n{output}"
    
    return {"text": prompt}

formatted_data = [format_prompt(ex) for ex in data]
dataset = Dataset.from_list(formatted_data)

print("🔧 Loading model and tokenizer...")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# Load model with 4-bit quantization for efficiency
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    load_in_4bit=True,
    torch_dtype=torch.float16,
    device_map="auto",
)

# Prepare model for training
model = prepare_model_for_kbit_training(model)

# LoRA configuration
lora_config = LoraConfig(
    r=16,  # LoRA rank
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)

print("✅ Model loaded and configured")
print(f"📊 Trainable parameters: {model.print_trainable_parameters()}")

# Tokenize dataset
def tokenize_function(examples):
    return tokenizer(
        examples["text"],
        truncation=True,
        max_length=MAX_LENGTH,
        padding="max_length"
    )

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=NUM_EPOCHS,
    per_device_train_batch_size=BATCH_SIZE,
    learning_rate=LEARNING_RATE,
    logging_steps=10,
    save_steps=100,
    save_total_limit=2,
    fp16=True,
    report_to="none",
)

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=data_collator,
)

print("\n🎯 Starting training...")
print(f"⏱️  This will take 2-8 hours depending on your hardware")
print("=" * 60)

# Train
trainer.train()

print("\n✅ Training complete!")
print(f"💾 Saving model to {OUTPUT_DIR}")

# Save model
model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print("\n🎉 Fine-tuning complete!")
print(f"📁 Model saved to: {OUTPUT_DIR}")
print("\nNext steps:")
print("1. Run: python3 scripts/export_to_ollama.py")
print("2. Test your custom model")
