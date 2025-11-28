#!/bin/bash

echo "🚀 Starting HDD Cleaner Setup..."

# 1. Ensure script is run from project root
if [ ! -d "src" ]; then
    echo "❌ Please run this script from the project root (hdd_cleaner/)"
    exit 1
fi

# 2. Create Python virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# 3. Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# 4. Upgrade pip
pip install --upgrade pip

# 5. Install all dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# 6. Ensure data folders exist
echo "📁 Creating required folders..."
mkdir -p data/raw data/processed data/logs

# 7. Verify HDD mount path
HDD_PATH="/mnt/myhdd"
if mountpoint -q "$HDD_PATH"; then
    echo "✅ HDD is mounted at $HDD_PATH"
else
    echo "⚠ HDD NOT mounted at $HDD_PATH"
    echo "   Please mount the HDD manually:"
    echo "   sudo mkdir -p /mnt/myhdd"
    echo "   sudo mount /dev/sdb1 /mnt/myhdd"
fi

echo "🔍 Checking Python entry point..."
if [ -f "src/main.py" ]; then
    echo "   main.py found."
else
    echo "❌ main.py missing."
    exit 1
fi

# 8. Make script executable
chmod +x setup.sh

echo "🎉 Setup complete!"
echo "👉 To run the project:"
echo "source venv/bin/activate && python src/main.py"
