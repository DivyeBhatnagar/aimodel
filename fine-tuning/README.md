# Fine-Tune LLaMA 3 for CodePilot

## Time Breakdown

- **Setup:** 15 minutes (you do this now)
- **Data Prep:** 30 minutes (collect examples)
- **Training:** 2-8 hours (runs automatically)
- **Testing:** 15 minutes

**Total Active Time:** 1 hour  
**Total Wait Time:** 2-8 hours (computer does the work)

---

## Quick Start (15 Minutes)

### Step 1: Install Dependencies
```bash
cd fine-tuning
pip3 install torch transformers datasets peft bitsandbytes accelerate
```

### Step 2: Add Training Data
Edit `data/training_data.json` with your examples (minimum 50, ideal 500+)

### Step 3: Run Training
```bash
python3 scripts/train.py
```

### Step 4: Deploy to Ollama
```bash
python3 scripts/export_to_ollama.py
```

---

## Hardware Requirements

**Minimum:**
- 16GB RAM
- 8GB GPU (or use CPU, slower)
- 20GB free disk space

**Recommended:**
- 32GB RAM
- 16GB+ GPU (RTX 3090/4090)
- 50GB free disk space

**No GPU?** Use Google Colab (free) - instructions included

---

## Cost Options

1. **Your Mac (Free)** - Slow but works, 8-12 hours
2. **Google Colab Free** - 4-6 hours
3. **RunPod GPU ($1/hr)** - 2-3 hours = $2-3 total
4. **Lambda Labs ($1.50/hr)** - 2-3 hours = $3-5 total

---

## What You'll Get

After training:
- Custom LLaMA 3 model trained on YOUR data
- Deployed to Ollama as "codepilot-custom"
- Can legitimately say "my custom AI model"
- Better at YOUR specific use cases

---

## Next Steps

1. Run setup commands below
2. Add your training data
3. Start training (runs overnight)
4. Wake up to your custom model
