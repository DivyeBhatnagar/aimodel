## 1-Hour Setup Guide

### Minute 0-15: Install & Setup

```bash
cd fine-tuning

# Install Python dependencies
pip3 install torch transformers datasets peft bitsandbytes accelerate

# Or use requirements.txt
pip3 install -r requirements.txt
```

### Minute 15-45: Prepare Training Data

Edit `data/training_data.json` with YOUR examples:

**Minimum:** 50 examples  
**Good:** 200 examples  
**Excellent:** 500+ examples

Format:
```json
{
  "instruction": "What you want the AI to do",
  "input": "Optional context",
  "output": "The ideal response"
}
```

**Pro Tip:** Use your existing API logs, documentation, or code examples

### Minute 45-60: Start Training

```bash
# Start training (runs for 2-8 hours)
python3 scripts/train.py

# Go do something else - it runs automatically
```

### After Training: Deploy

```bash
# Export to Ollama
python3 scripts/export_to_ollama.py

# Test it
ollama run codepilot-custom

# Update your backend
# In server.js, change model to "codepilot-custom"
```

---

## No GPU? Use Google Colab

1. Open: https://colab.research.google.com
2. Upload `scripts/train.py`
3. Upload `data/training_data.json`
4. Run in Colab (free GPU)
5. Download trained model
6. Import to Ollama

---

## Cost Breakdown

| Option | Time | Cost |
|--------|------|------|
| Your Mac (CPU) | 8-12 hrs | Free |
| Your Mac (GPU) | 4-6 hrs | Free |
| Google Colab Free | 4-6 hrs | Free |
| RunPod GPU | 2-3 hrs | $2-3 |
| Lambda Labs | 2-3 hrs | $3-5 |

---

## What You Get

✅ Custom AI model trained on YOUR data  
✅ Can say "my custom AI model"  
✅ Better at YOUR specific tasks  
✅ Runs locally, fully offline  
✅ No API costs  

---

## Troubleshooting

**"Out of memory"**
- Reduce BATCH_SIZE in train.py (try 2 or 1)
- Use Google Colab instead

**"Model not found"**
- Download LLaMA 3 first: `ollama pull llama3`
- Or use local model path

**"Training too slow"**
- Use cloud GPU (RunPod/Lambda)
- Reduce dataset size for testing

---

## Next Steps

1. Collect more training data over time
2. Retrain monthly with new examples
3. A/B test against base model
4. Track performance improvements
