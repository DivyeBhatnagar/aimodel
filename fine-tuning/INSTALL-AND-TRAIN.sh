#!/bin/bash

echo "🚀 Installing Training Dependencies + Starting Training"
echo "========================================================"
echo ""
echo "⚠️  WARNING: This will take 5-10 minutes to install"
echo "    Then training will run for 2-8 hours"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Cancelled."
    exit 1
fi

echo ""
echo "📦 Installing PyTorch and dependencies..."
echo "This may take 5-10 minutes..."
echo ""

# Install dependencies
pip3 install torch transformers peft bitsandbytes accelerate datasets

echo ""
echo "✅ Dependencies installed!"
echo ""
echo "🎯 Starting training..."
echo "This will take 2-8 hours depending on your hardware"
echo ""
echo "You can close this terminal and it will keep running"
echo "Or press Ctrl+C to stop"
echo ""

# Start training
python3 scripts/train.py

echo ""
echo "✅ Training complete!"
echo ""
echo "Next step: python3 scripts/export_to_ollama.py"
