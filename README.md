# 🎭 SpongeBob AI Demo - BCS Educational Project

An interactive AI demonstration for Berlin Cosmopolitan School (BCS) primary students that showcases:
- **AI voice cloning** - Real-time voice synthesis mimicking SpongeBob
- **AI personality modeling** - Text generation matching character behavior
- **Digital literacy education** - Teaching critical thinking about AI-generated content

Perfect for teaching grades 1-6 about AI capabilities and online safety!

## 🌟 Features

- 🎤 **Real-time voice cloning** using Coqui XTTS model
- 🤖 **AI personality engine** powered by Google Gemini 2.0
- 💬 **Interactive chat interface** with SpongeBob character
- 📚 **Educational demo scripts** for different age groups
- 🎓 **Digital literacy focus** - teaching kids to question AI-generated content
- 🚀 **MPS GPU acceleration** for Mac (Apple Silicon)

## 📋 Prerequisites

- **Python 3.9+** (Python 3.11 recommended)
- **macOS** with Apple Silicon (M1/M2/M3) for MPS acceleration, or any system with CUDA/CPU
- **ffmpeg** for audio processing
- **Google Gemini API key** (free at [ai.google.dev](https://ai.google.dev/))

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/malibio/bcs-ai-demo.git
cd bcs-ai-demo

# Run the setup script
./setup.sh

# Edit .env and add your Gemini API key
nano .env  # or use your preferred editor

# Start the voice server (Terminal 1)
source venv/bin/activate
python voice_server.py

# Start the web app (Terminal 2)
source venv/bin/activate
python app.py

# Open in browser
open http://127.0.0.1:5000
```

### Option 2: Manual Setup

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3. Install ffmpeg (if not installed)
brew install ffmpeg  # macOS
# or
sudo apt install ffmpeg  # Linux

# 4. Configure API key
cp .env.example .env
# Edit .env and add your Gemini API key

# 5. Create audio directory
mkdir -p static/audio

# 6. Start both servers
# Terminal 1:
python voice_server.py

# Terminal 2:
python app.py
```

## 🏗️ Project Structure

```
bcs-ai-demo/
├── app.py                      # Main Flask web application
├── voice_server.py             # Voice cloning service (XTTS)
├── voice_service.py            # Voice generation utilities
├── requirements.txt            # Python dependencies
├── setup.sh                    # Automated setup script
├── .env.example                # Environment variables template
├── .env                        # Your API keys (create from .env.example)
│
├── templates/
│   └── index.html              # Web interface
│
├── static/
│   ├── style.css               # Styling
│   ├── spongebob-image.png     # Character image
│   └── audio/                  # Generated voice files (auto-created)
│       └── .gitkeep
│
├── DEMO_SCRIPT_8MIN.md         # 8-minute parent-led demo script
├── DEMO_SCRIPT.md              # Full educational demo script
└── README.md                   # This file
```

## 🎯 How It Works

### Architecture

```
User Input → Gemini AI (Text) → XTTS Model (Voice) → Browser (Audio)
```

1. **Text Generation Pipeline:**
   - User types a question
   - Gemini 2.0 Flash generates response with SpongeBob personality
   - Response sent to voice server

2. **Voice Cloning Pipeline:**
   - Text converted to numerical embeddings
   - XTTS model predicts audio patterns based on SpongeBob voice sample
   - WAV audio file generated and cached
   - Browser plays the cloned voice

### Technical Details

- **AI Text Model:** Google Gemini 2.0 Flash (via API)
- **Voice Model:** Coqui XTTS v2 (multilingual, multi-dataset)
- **Acceleration:** MPS (Metal Performance Shaders) for Apple Silicon
- **Web Framework:** Flask
- **Audio Format:** WAV files served via static directory

## 📖 Running the Demo

The project includes two demo scripts for parent-led presentations:

- **`DEMO_SCRIPT_8MIN.md`** - Streamlined 8-minute interactive demo
- **`DEMO_SCRIPT.md`** - Full 15-20 minute educational presentation

Both scripts include:
- Age-appropriate talking points (grades 1-6)
- Technical explanations (numbers, patterns, prediction)
- Digital safety lessons (question, check, tell an adult)
- Interactive Q&A format

### Demo Flow (8 minutes)

1. **Hook** (2 min) - Show AI SpongeBob, explain how it works
2. **Student Q&A** (3 min) - Let kids ask SpongeBob questions
3. **Safety Lesson** (2 min) - Teach critical thinking about AI
4. **Wrap-up** (1 min) - Quick quiz and takeaways

## 🔧 Configuration

### Environment Variables (`.env`)

```bash
# Required
GEMINI_API_KEY=your_gemini_api_key_here
```

### Character Personality

Edit `app.py` to customize SpongeBob's personality prompt:

```python
CHARACTERS = {
    'spongebob': {
        'name': 'SpongeBob SquarePants',
        'prompt': """You are SpongeBob..."""
    }
}
```

### Voice Sample

The SpongeBob voice sample is learned by the XTTS model. To improve quality:

1. Use `improve_voice_sample.py` to process audio clips
2. Place improved samples in the project root
3. Update `voice_server.py` reference sample path

## 🎓 Educational Value

This demo teaches students:

### Technical Concepts
- How AI uses numbers and patterns to predict words
- Voice cloning through audio pattern matching
- Machine learning prediction models

### Digital Literacy
- ⚠️ AI-generated content can look/sound real but isn't
- ✅ Always verify sources (especially for requests)
- 🛡️ Tell adults about suspicious online content

### Critical Thinking
- Question authenticity of media
- Understand technology capabilities and limitations
- Recognize responsible vs. malicious AI use

## 🐛 Troubleshooting

### Voice server won't start
```bash
# Check if port 5001 is in use
lsof -i :5001

# Kill existing process if needed
kill -9 <PID>
```

### "Module not found" errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Audio not playing
- Check browser console for errors
- Ensure voice_server.py is running on port 5001
- Verify `static/audio/` directory exists
- Check browser autoplay policies (may require user interaction)

### Slow voice generation
- First generation always slower (model loading)
- MPS acceleration requires Apple Silicon Mac
- Consider using CPU mode on other systems

### API errors
- Verify GEMINI_API_KEY in `.env`
- Check API quota at [ai.google.dev](https://ai.google.dev/)
- Ensure `.env` file is in project root

## 🔒 Security & Privacy

- **API Keys:** Never commit `.env` to git (already in `.gitignore`)
- **Audio Files:** Generated files stored locally, not in git
- **Student Privacy:** No data collection or logging
- **Educational Use:** This demo is for educational purposes only

## 📜 License

Educational project for BCS. SpongeBob SquarePants is © Nickelodeon. This is a non-commercial educational demonstration.

## 🤝 Contributing

This is a parent-led educational initiative. If you're a BCS parent or educator:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📞 Support

For BCS parents and educators:
- Check demo scripts in `DEMO_SCRIPT_8MIN.md`
- Review troubleshooting section above
- Open GitHub issues for technical problems

## 🙏 Acknowledgments

- **BCS Community** - For supporting STEM education
- **Google Gemini** - For AI text generation API
- **Coqui AI** - For open-source XTTS voice cloning
- **Primary Students** - Our curious learners!

---

**Built with ❤️ for BCS by parent volunteers**

*Teaching the next generation to be smart, creative, and critical thinkers in an AI world.*
