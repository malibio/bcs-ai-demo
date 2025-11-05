#!/bin/bash

# SpongeBob AI Demo Setup Script
# This script sets up the development environment for the BCS AI Demo

set -e  # Exit on error

echo "🎭 Setting up SpongeBob AI Demo..."
echo ""

# Check Python version
echo "📋 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Found Python $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "ℹ️  Virtual environment already exists"
fi
echo ""

# Activate virtual environment and install dependencies
echo "📥 Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
echo "🔑 Setting up environment variables..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ Created .env file from template"
    echo ""
    echo "⚠️  IMPORTANT: Please edit .env and add your Gemini API key!"
    echo "   Get your API key from: https://ai.google.dev/"
else
    echo "ℹ️  .env file already exists"
fi
echo ""

# Create static/audio directory
echo "📁 Creating audio directory..."
mkdir -p static/audio
echo "✅ Audio directory ready"
echo ""

# Check if ffmpeg is installed (needed for audio processing)
echo "🔍 Checking for ffmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  Warning: ffmpeg is not installed. Audio processing may not work."
    echo "   Install with: brew install ffmpeg (macOS) or apt install ffmpeg (Linux)"
else
    echo "✅ ffmpeg is installed"
fi
echo ""

echo "✨ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Edit .env and add your Gemini API key"
echo "  2. Start the voice server: source venv/bin/activate && python voice_server.py"
echo "  3. In another terminal, start the app: source venv/bin/activate && python app.py"
echo "  4. Open http://127.0.0.1:5000 in your browser"
echo ""
echo "For the demo, see DEMO_SCRIPT_8MIN.md"
echo ""
