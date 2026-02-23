# ⚡ Ultra Quick Start - 2 Commands Only!

## The Absolute Fastest Way

### Command 1: Setup + Load Data (5 minutes)
```bash
cd fine-tuning
bash ONE-COMMAND-START.sh
```

This automatically:
- ✅ Installs all dependencies
- ✅ Downloads 600 training examples
- ✅ Formats everything correctly

### Command 2: Train (2-8 hours automatic)
```bash
python3 scripts/train.py
```

Then go to sleep. Wake up to your custom model.

---

## That's It!

**Total commands:** 2  
**Your active time:** 5 minutes  
**Computer work time:** 2-8 hours (automatic)  
**Cost:** $0

---

## After Training (1 command)

```bash
python3 scripts/export_to_ollama.py
```

Now you have "codepilot-custom" model!

---

## Update Your Backend (30 seconds)

In `server.js`, line 23, change:
```javascript
const { prompt, model = 'codepilot-custom', temperature = 0.7, max_tokens } = req.body;
```

Restart server:
```bash
npm start
```

Done! Your custom AI is live.

---

## What You Get

✅ Custom AI model trained on 600 coding examples  
✅ Optimized for Python, JavaScript, SQL  
✅ Can say "my custom AI model"  
✅ Runs completely offline  
✅ Zero ongoing costs  

---

## Comparison

### Old Way (Manual):
1. Research datasets (1 hour)
2. Download manually (30 min)
3. Format data (1 hour)
4. Fix errors (30 min)
5. Install dependencies (15 min)
6. Configure training (30 min)
7. Start training

**Total: 4+ hours of work**

### New Way (Automatic):
1. Run `bash ONE-COMMAND-START.sh`
2. Run `python3 scripts/train.py`

**Total: 5 minutes of work**

---

## Troubleshooting

**"Command not found"**
```bash
cd fine-tuning
chmod +x ONE-COMMAND-START.sh
bash ONE-COMMAND-START.sh
```

**"pip3 not found"**
```bash
# Install Python first
brew install python3
```

**"Out of memory during training"**
- Use Google Colab (free GPU)
- Or reduce batch size in train.py

---

## Next Level

Want more examples? Edit the script:

```bash
# In scripts/load_dataset.py, line 280:
"max_samples": 1000  # instead of 300
```

Then rerun:
```bash
python3 scripts/load_dataset.py
# Choose option 6
```

---

## The Bottom Line

**2 commands. 5 minutes. Your own AI model.**

No excuses. Just do it! 🚀
