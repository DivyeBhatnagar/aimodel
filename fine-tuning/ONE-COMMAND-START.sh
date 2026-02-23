#!/bin/bash

echo "🚀 CodePilot Fine-Tuning - One Command Setup"
echo "=============================================="
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -q torch transformers datasets peft bitsandbytes accelerate requests

echo ""
echo "✅ Dependencies installed!"
echo ""

# Load dataset
echo "📥 Loading training dataset (600 examples)..."
python3 scripts/load_dataset.py <<EOF
6
EOF

echo ""
echo "✅ Dataset loaded!"
echo ""
echo "🎯 Ready to train!"
echo ""
echo "Next step:"
echo "  python3 scripts/train.py"
echo ""
echo "This will take 2-8 hours (runs automatically)"
echo "You can close this terminal and let it run"
echo ""
