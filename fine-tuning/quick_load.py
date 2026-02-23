#!/usr/bin/env python3
"""Quick load CodeAlpaca dataset"""

import json
from datasets import load_dataset

print("📥 Loading CodeAlpaca-20k dataset...")
print("=" * 60)

# Load dataset
dataset = load_dataset("sahil2801/CodeAlpaca-20k", split="train")

# Take 500 samples for faster training
dataset = dataset.select(range(500))

print(f"✅ Loaded {len(dataset)} examples")

# Convert to our format
training_data = []
for item in dataset:
    training_data.append({
        "instruction": item.get('instruction', ''),
        "input": item.get('input', ''),
        "output": item.get('output', '')
    })

# Save
with open('./data/training_data.json', 'w') as f:
    json.dump(training_data, f, indent=2)

print(f"💾 Saved to data/training_data.json")
print(f"\n✅ Ready to train!")
print(f"\nNext: python3 scripts/train.py")
