#!/usr/bin/env python3
"""
Load training datasets from various sources
No need to manually create training data!
"""

import json
import requests
from datasets import load_dataset
import os

OUTPUT_FILE = "./data/training_data.json"

print("📥 Dataset Loader for CodePilot")
print("=" * 60)

# ============================================
# OPTION 1: Load from Hugging Face
# ============================================
def load_from_huggingface(dataset_name, split="train", max_samples=1000):
    """
    Load dataset from Hugging Face Hub
    
    Popular coding datasets:
    - "iamtarun/python_code_instructions_18k_alpaca"
    - "sahil2801/CodeAlpaca-20k"
    - "codeparrot/github-code"
    - "bigcode/the-stack-dedup"
    """
    print(f"\n📦 Loading from Hugging Face: {dataset_name}")
    
    try:
        dataset = load_dataset(dataset_name, split=split)
        
        # Take only max_samples
        if len(dataset) > max_samples:
            dataset = dataset.select(range(max_samples))
        
        print(f"✅ Loaded {len(dataset)} examples")
        
        # Convert to our format
        training_data = []
        for item in dataset:
            # Adapt based on dataset structure
            if 'instruction' in item and 'output' in item:
                training_data.append({
                    "instruction": item['instruction'],
                    "input": item.get('input', ''),
                    "output": item['output']
                })
            elif 'prompt' in item and 'completion' in item:
                training_data.append({
                    "instruction": item['prompt'],
                    "input": '',
                    "output": item['completion']
                })
            elif 'question' in item and 'answer' in item:
                training_data.append({
                    "instruction": item['question'],
                    "input": '',
                    "output": item['answer']
                })
        
        return training_data
        
    except Exception as e:
        print(f"❌ Error loading from Hugging Face: {e}")
        return []


# ============================================
# OPTION 2: Load from URL (JSON)
# ============================================
def load_from_url(url):
    """
    Load dataset from a direct URL
    Expects JSON format: [{"instruction": "", "output": ""}, ...]
    """
    print(f"\n🌐 Loading from URL: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        print(f"✅ Loaded {len(data)} examples")
        
        return data
        
    except Exception as e:
        print(f"❌ Error loading from URL: {e}")
        return []


# ============================================
# OPTION 3: Load from GitHub
# ============================================
def load_from_github(repo, file_path, branch="main"):
    """
    Load dataset from GitHub repository
    
    Example:
    repo = "username/repo-name"
    file_path = "data/training.json"
    """
    url = f"https://raw.githubusercontent.com/{repo}/{branch}/{file_path}"
    print(f"\n🐙 Loading from GitHub: {repo}/{file_path}")
    
    return load_from_url(url)


# ============================================
# OPTION 4: Load from Google Drive
# ============================================
def load_from_google_drive(file_id):
    """
    Load dataset from Google Drive shared link
    
    Get file_id from share link:
    https://drive.google.com/file/d/FILE_ID_HERE/view
    """
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    print(f"\n📁 Loading from Google Drive: {file_id}")
    
    return load_from_url(url)


# ============================================
# OPTION 5: Load Multiple Sources
# ============================================
def load_multiple_sources(sources):
    """
    Combine datasets from multiple sources
    """
    all_data = []
    
    for source in sources:
        if source['type'] == 'huggingface':
            data = load_from_huggingface(
                source['name'],
                source.get('split', 'train'),
                source.get('max_samples', 1000)
            )
        elif source['type'] == 'url':
            data = load_from_url(source['url'])
        elif source['type'] == 'github':
            data = load_from_github(
                source['repo'],
                source['file_path'],
                source.get('branch', 'main')
            )
        elif source['type'] == 'google_drive':
            data = load_from_google_drive(source['file_id'])
        
        all_data.extend(data)
    
    return all_data


# ============================================
# SAVE DATASET
# ============================================
def save_dataset(data, output_file=OUTPUT_FILE):
    """Save dataset to JSON file"""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"\n💾 Saved {len(data)} examples to {output_file}")


# ============================================
# PRE-CONFIGURED DATASETS
# ============================================

# Coding instruction datasets
CODING_DATASETS = {
    "python_alpaca": {
        "type": "huggingface",
        "name": "iamtarun/python_code_instructions_18k_alpaca",
        "max_samples": 500
    },
    "code_alpaca": {
        "type": "huggingface",
        "name": "sahil2801/CodeAlpaca-20k",
        "max_samples": 500
    },
    "sql_instructions": {
        "type": "huggingface",
        "name": "Clinton/Text-to-sql-v1",
        "max_samples": 200
    }
}


# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    print("\n🎯 Choose a dataset source:\n")
    print("1. Hugging Face - Python Code Instructions (500 examples)")
    print("2. Hugging Face - Code Alpaca (500 examples)")
    print("3. Hugging Face - SQL Instructions (200 examples)")
    print("4. Custom URL (provide your own)")
    print("5. GitHub Repository (provide repo details)")
    print("6. Combine multiple sources")
    print("7. Use example dataset (5 examples)")
    
    choice = input("\nEnter choice (1-7): ").strip()
    
    training_data = []
    
    if choice == "1":
        training_data = load_from_huggingface(
            "iamtarun/python_code_instructions_18k_alpaca",
            max_samples=500
        )
    
    elif choice == "2":
        training_data = load_from_huggingface(
            "sahil2801/CodeAlpaca-20k",
            max_samples=500
        )
    
    elif choice == "3":
        training_data = load_from_huggingface(
            "Clinton/Text-to-sql-v1",
            max_samples=200
        )
    
    elif choice == "4":
        url = input("Enter dataset URL: ").strip()
        training_data = load_from_url(url)
    
    elif choice == "5":
        repo = input("Enter GitHub repo (username/repo): ").strip()
        file_path = input("Enter file path in repo: ").strip()
        training_data = load_from_github(repo, file_path)
    
    elif choice == "6":
        # Combine multiple sources
        sources = [
            {
                "type": "huggingface",
                "name": "iamtarun/python_code_instructions_18k_alpaca",
                "max_samples": 300
            },
            {
                "type": "huggingface",
                "name": "sahil2801/CodeAlpaca-20k",
                "max_samples": 300
            }
        ]
        training_data = load_multiple_sources(sources)
    
    elif choice == "7":
        print("\n✅ Using existing example dataset")
        exit(0)
    
    else:
        print("❌ Invalid choice")
        exit(1)
    
    if training_data:
        save_dataset(training_data)
        print("\n✅ Dataset ready for training!")
        print(f"\nNext step: python3 scripts/train.py")
    else:
        print("\n❌ No data loaded")
