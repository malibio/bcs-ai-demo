#!/usr/bin/env python3
"""
Voice cloning service for SpongeBob AI demo
Runs in separate Python 3.11 environment
"""
import torch
from TTS.api import TTS
import warnings
import sys
import json
import os

# Suppress warnings
warnings.filterwarnings('ignore')

# Suppress TTS library output by redirecting stdout temporarily
class SuppressOutput:
    def __enter__(self):
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = self._original_stdout
        sys.stderr = self._original_stderr

# Fix for PyTorch 2.6+ weights_only issue
import torch.serialization
torch.serialization.add_safe_globals(['TTS.tts.configs.xtts_config.XttsConfig'])

# Monkey patch torch.load
original_torch_load = torch.load
def patched_load(*args, **kwargs):
    kwargs['weights_only'] = False
    return original_torch_load(*args, **kwargs)
torch.load = patched_load

# Initialize TTS model (do this once at startup) - suppress output
with SuppressOutput():
    device = "cpu"  # CPU is faster than MPS for this model
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Voice sample path
VOICE_SAMPLE = "spongebob-sample.wav"

def generate_speech(text, output_path):
    """Generate speech with cloned voice"""
    import time
    try:
        start_time = time.time()
        with SuppressOutput():
            tts.tts_to_file(
                text=text,
                speaker_wav=VOICE_SAMPLE,
                language="en",
                file_path=output_path
            )
        elapsed = time.time() - start_time
        print(f"Voice generation took {elapsed:.2f} seconds", file=sys.stderr)
        return True
    except Exception as e:
        print(f"Error generating voice: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    # Read input from stdin (text to generate)
    input_data = json.loads(sys.stdin.read())
    text = input_data.get("text", "")
    output_file = input_data.get("output", "output.wav")

    success = generate_speech(text, output_file)

    # Return result as JSON
    result = {
        "success": success,
        "output_file": output_file if success else None
    }
    print(json.dumps(result))
