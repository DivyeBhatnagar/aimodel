# Dataset Sources - No Manual Work Required!

Instead of creating training data manually, load it from these sources:

---

## Quick Start

```bash
# Install dataset library
pip3 install datasets

# Run the loader
python3 scripts/load_dataset.py

# Choose a source and it downloads automatically!
```

---

## Option 1: Hugging Face Datasets (Recommended)

### Popular Coding Datasets

**Python Code Instructions (18K examples)**
```python
Dataset: "iamtarun/python_code_instructions_18k_alpaca"
Size: 18,000 examples
Focus: Python coding tasks
```

**Code Alpaca (20K examples)**
```python
Dataset: "sahil2801/CodeAlpaca-20k"
Size: 20,000 examples
Focus: Multi-language coding
```

**SQL Instructions**
```python
Dataset: "Clinton/Text-to-sql-v1"
Size: 5,000+ examples
Focus: SQL query generation
```

**JavaScript/Web Development**
```python
Dataset: "codeparrot/github-code"
Filter: JavaScript files
Focus: Real-world JS code
```

### How to Use:
```bash
python3 scripts/load_dataset.py
# Choose option 1, 2, or 3
```

---

## Option 2: Load from URL

Host your dataset anywhere and load it:

```python
# Your dataset URL (JSON format)
url = "https://example.com/my-dataset.json"

# Run loader
python3 scripts/load_dataset.py
# Choose option 4, enter URL
```

**JSON Format:**
```json
[
  {
    "instruction": "Create a login form",
    "input": "",
    "output": "Here's a login form..."
  }
]
```

---

## Option 3: Load from GitHub

Store your dataset in a GitHub repo:

```bash
# Public repo structure:
# username/my-datasets
#   └── data/
#       └── training.json

python3 scripts/load_dataset.py
# Choose option 5
# Enter: username/my-datasets
# Enter: data/training.json
```

---

## Option 4: Load from Google Drive

1. Upload your dataset to Google Drive
2. Right-click → Share → Get link
3. Extract file ID from URL:
   ```
   https://drive.google.com/file/d/FILE_ID_HERE/view
   ```
4. Use in script (modify load_dataset.py):
   ```python
   load_from_google_drive("FILE_ID_HERE")
   ```

---

## Option 5: Combine Multiple Sources

Mix datasets for better coverage:

```python
# Edit load_dataset.py, option 6:
sources = [
    {
        "type": "huggingface",
        "name": "iamtarun/python_code_instructions_18k_alpaca",
        "max_samples": 300
    },
    {
        "type": "url",
        "url": "https://your-site.com/custom-data.json"
    },
    {
        "type": "github",
        "repo": "username/repo",
        "file_path": "data/training.json"
    }
]
```

---

## Pre-Made Dataset Collections

### For Web Development
```python
# Combine these:
- Code Alpaca (general coding)
- JavaScript examples from GitHub
- React component examples
- API endpoint patterns
```

### For Data Science
```python
# Combine these:
- Python instructions
- SQL queries
- Data analysis examples
- ML algorithm implementations
```

### For Full-Stack
```python
# Combine these:
- Frontend (React, Vue)
- Backend (Node, Python)
- Database (SQL, MongoDB)
- DevOps (Docker, CI/CD)
```

---

## Custom Dataset APIs

### Stack Overflow
```python
# Use Stack Exchange API
url = "https://api.stackexchange.com/2.3/questions"
# Filter by tags: python, javascript, etc.
```

### GitHub Code Search
```python
# Use GitHub API
url = "https://api.github.com/search/code"
# Search for specific patterns
```

### Your Own API Logs
```python
# Export from your existing API
url = "https://your-api.com/export/training-data"
```

---

## Dataset Quality Tips

### Good Datasets:
✅ 500+ examples minimum
✅ Diverse examples (different tasks)
✅ Clean, well-formatted code
✅ Clear instructions
✅ Realistic use cases

### Avoid:
❌ Too small (<50 examples)
❌ Repetitive examples
❌ Outdated code patterns
❌ Unclear instructions
❌ Toy examples only

---

## Recommended Combinations

### Starter Pack (Free, 1000 examples)
```bash
python3 scripts/load_dataset.py
# Choose option 6 (combine)
# Gets: 500 Python + 500 Code Alpaca
```

### Professional Pack (Free, 2000 examples)
```python
- 500 Python instructions
- 500 Code Alpaca
- 500 SQL queries
- 500 Your custom data
```

### Enterprise Pack (Custom)
```python
- Public datasets (1000)
- Your API logs (2000)
- Your documentation (500)
- Your code examples (500)
Total: 4000 examples
```

---

## No Dataset? Use These Free Sources

1. **Hugging Face Hub**
   - https://huggingface.co/datasets
   - Search: "code", "programming", "instructions"

2. **GitHub Awesome Lists**
   - https://github.com/topics/awesome
   - Find curated code examples

3. **Kaggle Datasets**
   - https://www.kaggle.com/datasets
   - Search: "code", "programming"

4. **Papers with Code**
   - https://paperswithcode.com/datasets
   - Research datasets

---

## Quick Commands

### Load Python dataset (500 examples)
```bash
python3 scripts/load_dataset.py
# Enter: 1
```

### Load from your URL
```bash
python3 scripts/load_dataset.py
# Enter: 4
# Paste your URL
```

### Combine multiple sources
```bash
python3 scripts/load_dataset.py
# Enter: 6
```

---

## After Loading

```bash
# Check what was loaded
cat data/training_data.json | head -n 50

# Start training
python3 scripts/train.py

# That's it!
```

---

## Cost: $0

All these datasets are:
- ✅ Free to use
- ✅ Open source
- ✅ No API keys needed
- ✅ No rate limits

---

## Bottom Line

**You don't need to create training data manually!**

1. Run `python3 scripts/load_dataset.py`
2. Choose a source
3. Wait 1-2 minutes for download
4. Start training

**Total time: 5 minutes instead of hours**
