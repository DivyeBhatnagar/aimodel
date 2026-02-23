# ✅ Dataset Loaded! Ready to Train

## Current Status

✅ **Dataset:** CodeAlpaca-20k (500 examples)  
✅ **Location:** `data/training_data.json`  
✅ **Format:** Ready for training  

---

## Next Steps

### Option 1: Train on Your Mac (Free, Slow)

**Install dependencies (one time, 5-10 min):**
```bash
pip3 install torch transformers peft bitsandbytes accelerate
```

**Start training (2-8 hours):**
```bash
python3 scripts/train.py
```

---

### Option 2: Train on Google Colab (Free, Fast)

**Why Colab?**
- ✅ Free GPU
- ✅ 2-4 hours instead of 8-12
- ✅ No local resources used
- ✅ Pre-installed libraries

**Steps:**

1. **Go to Google Colab:**
   ```
   https://colab.research.google.com
   ```

2. **Create new notebook**

3. **Upload files:**
   - `scripts/train.py`
   - `data/training_data.json`

4. **Run in first cell:**
   ```python
   !pip install transformers peft bitsandbytes accelerate datasets
   ```

5. **Run in second cell:**
   ```python
   !python train.py
   ```

6. **Wait 2-4 hours**

7. **Download trained model**

8. **Import to Ollama on your Mac**

---

### Option 3: Cloud GPU (Fastest, $2-5)

**RunPod (Recommended):**
1. Go to: https://runpod.io
2. Create account
3. Deploy GPU pod ($0.69/hr)
4. Upload your files
5. Run training (2-3 hours)
6. Download model
7. Cost: ~$2-3 total

---

## What Happens During Training?

1. **Loading model** (5-10 min)
   - Downloads LLaMA 3 base model
   - Prepares for training

2. **Training** (2-8 hours)
   - Learns from your 500 examples
   - Saves checkpoints every 100 steps
   - Shows progress

3. **Saving** (2-5 min)
   - Saves your custom model
   - Ready to deploy

---

## After Training

```bash
# Export to Ollama
python3 scripts/export_to_ollama.py

# Test it
ollama run codepilot-custom

# Update your backend
# In server.js: model: "codepilot-custom"
```

---

## Time & Cost Comparison

| Method | Time | Cost | Difficulty |
|--------|------|------|------------|
| Your Mac (CPU) | 8-12 hrs | $0 | Easy |
| Your Mac (GPU) | 4-6 hrs | $0 | Easy |
| Google Colab | 2-4 hrs | $0 | Medium |
| RunPod | 2-3 hrs | $2-3 | Medium |
| Lambda Labs | 2-3 hrs | $3-5 | Medium |

---

## Recommended Path

**For first time:**
→ Google Colab (free + fast)

**For regular updates:**
→ Your Mac overnight (free + automatic)

**For production:**
→ RunPod/Lambda (fast + cheap)

---

## Install Training Dependencies Now

```bash
# This takes 5-10 minutes
pip3 install torch transformers peft bitsandbytes accelerate

# Then start training
python3 scripts/train.py
```

---

## Need Help?

**Check if dependencies installed:**
```bash
python3 -c "import torch; print('PyTorch OK')"
python3 -c "import transformers; print('Transformers OK')"
```

**Check dataset:**
```bash
cat data/training_data.json | head -n 20
```

**Monitor training:**
Training will show progress bars and loss values. Lower loss = better learning.

---

## The Bottom Line

**Dataset is ready!** ✅

Now choose:
- Install dependencies + train locally (free, slow)
- Use Google Colab (free, fast)
- Use cloud GPU (paid, fastest)

Your call! 🚀
