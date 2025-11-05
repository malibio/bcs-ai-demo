#!/usr/bin/env python3
"""
Create an improved voice sample with more laugh examples for better voice cloning.

Strategy:
1. Extract multiple segments from the full audio that include laughs
2. Combine them with normal speech to create a comprehensive training sample
3. Keep it under 30 seconds (TTS recommendation for XTTS)
"""

import subprocess
import sys

def check_ffmpeg():
    """Check if ffmpeg is available"""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ ffmpeg is not installed")
        print("\nTo install ffmpeg on macOS:")
        print("  brew install ffmpeg")
        print("\nAlternatively, you can manually extract audio segments using:")
        print("  - QuickTime Player (File > Open, then Edit > Trim)")
        print("  - Audacity (free audio editor)")
        return False

def extract_segments():
    """Extract audio segments with laughs"""
    if not check_ffmpeg():
        return False

    print("\n🎬 Extracting audio segments with laughs...")

    # These timestamps would need to be identified by listening to the audio
    # For now, let's extract a few segments to analyze
    segments = [
        # (start_time, duration, output_name, description)
        ("00:00:00", "10", "segment_1.wav", "First 10 seconds"),
        ("00:01:00", "10", "segment_2.wav", "At 1 minute"),
        ("00:05:00", "10", "segment_3.wav", "At 5 minutes"),
    ]

    for start, duration, output, desc in segments:
        print(f"  Extracting {desc}...")
        cmd = [
            'ffmpeg', '-i', 'sponge-bob-voice-clips.mp3',
            '-ss', start, '-t', duration,
            '-acodec', 'pcm_s16le', '-ar', '22050',
            output, '-y'
        ]
        subprocess.run(cmd, capture_output=True)

    print("✅ Extracted sample segments")
    print("\nNext steps:")
    print("1. Listen to these segments and identify which have good laughs")
    print("2. Use audio editing software to combine the best segments")
    print("3. Replace spongebob-sample.wav with the improved version")
    return True

if __name__ == '__main__':
    print("🔍 Analyzing voice sample situation...")
    print(f"   Current sample: spongebob-sample.wav")
    print(f"   Full audio: sponge-bob-voice-clips.mp3")

    if len(sys.argv) > 1 and sys.argv[1] == '--extract':
        extract_segments()
    else:
        if check_ffmpeg():
            print("\n✅ ffmpeg is available")
            print("\nTo extract sample segments, run:")
            print("  python improve_voice_sample.py --extract")
        else:
            print("\n📝 Recommendations for improving the voice sample:")
            print("\n1. Listen to the full audio (sponge-bob-voice-clips.mp3)")
            print("2. Find sections with:")
            print("   - Clear SpongeBob laugh ('Ahahaha!')")
            print("   - Varied speech patterns")
            print("   - Different emotions (excited, normal, questioning)")
            print("3. Extract 20-30 seconds that includes:")
            print("   - At least 2-3 good laugh examples")
            print("   - Normal conversational speech")
            print("   - A variety of tones")
            print("4. Save as spongebob-sample-improved.wav")
            print("5. Test with the voice server")
