# SpongeBob AI Demo - Educational Project

An educational app for kids (grades 1-5) that demonstrates how AI works by mimicking character personalities.

## Features

- Chat with AI SpongeBob that has his personality, catchphrases, and tone
- Text-to-speech audio responses (browser-based)
- Kid-friendly, colorful interface
- Educational - shows how AI learns patterns

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Your Gemini API Key

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### 3. Run the Application

```bash
python app.py
```

The app will start at: http://localhost:5000

## How It Works

1. **User Input**: Kid types a message to SpongeBob
2. **AI Processing**: Gemini 2.5 Pro generates a response matching SpongeBob's personality
3. **Text-to-Speech**: Browser's built-in TTS reads the response aloud
4. **Voice Cloning (Coming Soon)**: Will upgrade to use cloned SpongeBob voice

## Future Enhancements (Phase 2)

- [ ] Add voice cloning with Chatterbox/OpenVoice
- [ ] Clone actual SpongeBob voice from audio clips
- [ ] Add more characters (Chase from Paw Patrol, etc.)
- [ ] Record student voices and make them talk like characters
- [ ] Add visual explanations of how AI works

## Project Structure

```
bcs-ai-demo/
├── app.py                 # Flask backend with Gemini integration
├── templates/
│   └── index.html        # Frontend chat interface
├── static/
│   └── style.css         # Styling
├── requirements.txt      # Python dependencies
├── .env                  # API keys (create this)
└── README.md            # This file
```

## Educational Value

This project teaches kids that:
- AI learns patterns from data (training)
- AI can mimic personalities and speaking styles
- AI is predictive, not magical
- With the right data, AI can sound like anyone

Perfect for classroom demonstrations!
