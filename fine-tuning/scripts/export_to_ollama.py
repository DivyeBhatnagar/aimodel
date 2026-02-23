#!/usr/bin/env python3
"""
Export fine-tuned model to Ollama format
"""

import subprocess
import os

MODEL_DIR = "./models/codepilot-custom"
OLLAMA_MODEL_NAME = "codepilot-custom"

print("🔄 Exporting model to Ollama...")
print("=" * 60)

# Create Modelfile for Ollama
modelfile_content = f"""FROM ./models/codepilot-custom

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER top_k 40

SYSTEM You are CodePilot AI, a professional full-stack development assistant trained on custom data. You provide clear, accurate, and production-ready code solutions optimized for modern web development.
"""

modelfile_path = "./models/Modelfile"
with open(modelfile_path, 'w') as f:
    f.write(modelfile_content)

print(f"✅ Created Modelfile")

# Create Ollama model
print(f"\n📦 Creating Ollama model: {OLLAMA_MODEL_NAME}")
print("This may take a few minutes...")

try:
    result = subprocess.run(
        ["ollama", "create", OLLAMA_MODEL_NAME, "-f", modelfile_path],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"\n✅ Model exported successfully!")
        print(f"\n🎉 Your custom model is ready!")
        print(f"\nTest it with:")
        print(f"  ollama run {OLLAMA_MODEL_NAME}")
        print(f"\nOr update your backend to use it:")
        print(f'  model: "{OLLAMA_MODEL_NAME}"')
    else:
        print(f"❌ Error: {result.stderr}")
        
except FileNotFoundError:
    print("❌ Ollama not found. Make sure Ollama is installed and running.")
    print("Install: brew install ollama")
