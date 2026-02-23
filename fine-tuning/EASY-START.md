# 🚀 Easiest Way to Fine-Tune (No Manual Work!)

## The Problem
Creating training data manually takes hours.

## The Solution
Load datasets automatically from the internet!

---

## 3-Step Process (10 Minutes Total)

### Step 1: Install (2 minutes)
```bash
cd fine-tuning
pip3 install -r requirements.txt
```

### Step 2: Load Dataset (3 minutes)
```bash
python3 scripts/load_dataset.py
```

Choose option:
- **1** = Python code (500 examples) ← Recommended
- **2** = Multi-language code (500 examples)
- **3** = SQL queries (200 examples)
- **6** = Combine multiple (1000 examples) ← Best

### Step 3: Train (5 minutes to start)
```bash
python3 scripts/train.py
```

Then wait 2-8 hours (automatic).

---

## What Just Happened?

1. ✅ Downloaded 500-1000 coding examples
2. ✅ Formatted for training
3. ✅ Saved to `data/training_data.json`
4. ✅ Ready to train

**You did ZERO manual work!**

---

## Popular Dataset Choices

### For General Coding (Recommended)
```bash
python3 scripts/load_dataset.py
# Choose: 6 (combine multiple)
# Gets: 600 examples across Python, JS, SQL
```

### For Python Focus
```bash
python3 scripts/load_dataset.py
# Choose: 1
# Gets: 500 Python examples
```

### For Web Development
```bash
python3 scripts/load_dataset.py
# Choose: 2
# Gets: 500 multi-language examples
```

---

## Custom Dataset from URL

Have your own dataset? Load it:

```bash
python3 scripts/load_dataset.py
# Choose: 4
# Enter: https://your-site.com/dataset.json
```

**Format:**
```json
[
  {
    "instruction": "Create a login form",
    "input": "",
    "output": "Here's the code..."
  }
]
```

---

## After Training

```bash
# Deploy your custom model
python3 scripts/export_to_ollama.py

# Test it
ollama run codepilot-custom

# Update your backend
# In server.js: model: "codepilot-custom"
```

---

## Time Comparison

### Manual Way:
- Collect examples: 4-8 hours
- Format data: 1-2 hours
- **Total: 5-10 hours**

### Automatic Way:
- Run script: 2 minutes
- Choose dataset: 1 minute
- Download: 2 minutes
- **Total: 5 minutes**

**You save 5-10 hours!**

---

## Cost: $0

Everything is free:
- ✅ Datasets: Free (open source)
- ✅ Training: Free (your Mac or Google Colab)
- ✅ Deployment: Free (Ollama)

---

## Next Steps

1. **Right now:** Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```

2. **In 5 minutes:** Load dataset
   ```bash
   python3 scripts/load_dataset.py
   ```

3. **Tonight:** Start training (runs overnight)
   ```bash
   python3 scripts/train.py
   ```

4. **Tomorrow:** Deploy your custom model
   ```bash
   python3 scripts/export_to_ollama.py
   ```

---

## Questions?

**Q: Which dataset should I choose?**
A: Start with option 6 (combine multiple) for best results.

**Q: Can I add my own data later?**
A: Yes! Edit `data/training_data.json` and add more examples.

**Q: How long does training take?**
A: 2-8 hours depending on hardware. Runs automatically.

**Q: Does this cost money?**
A: No! Everything is free.

---

## The Bottom Line

**Old way:** Spend hours creating training data manually

**New way:** Run one command, get 500-1000 examples in 5 minutes

**Your choice is easy!** 🚀
