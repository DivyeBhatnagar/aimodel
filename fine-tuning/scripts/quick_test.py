#!/usr/bin/env python3
"""
Quick test of your fine-tuned model
"""

import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "codepilot-custom"  # or "llama3" for comparison

test_prompts = [
    "Create a React button component",
    "Write a Python function to sort a list",
    "Explain async/await in JavaScript"
]

print("🧪 Testing Your Custom Model")
print("=" * 60)

for i, prompt in enumerate(test_prompts, 1):
    print(f"\nTest {i}: {prompt}")
    print("-" * 60)
    
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    
    if response.status_code == 200:
        result = response.json()
        print(result['response'][:300] + "...")
    else:
        print(f"❌ Error: {response.status_code}")

print("\n" + "=" * 60)
print("✅ Testing complete!")
