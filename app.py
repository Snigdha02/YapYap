import sounddevice as sd
import numpy as np
import whisper
import tempfile
import scipy.io.wavfile
import time
import os
from datetime import datetime
import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU*")

# Limit OpenMP threads to avoid warning
os.environ["OMP_NUM_THREADS"] = "1"

# Config
DURATION = 10  # seconds per audio chunk
SAMPLERATE = 16000  # sample rate in Hz
LOG_FILE = "output/transcription_log.txt"

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Load Whisper model
model = whisper.load_model("base")

def record_audio_blocking(duration=DURATION, samplerate=SAMPLERATE):
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    return audio

def save_temp_wav(audio, samplerate=SAMPLERATE):
    temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    scipy.io.wavfile.write(temp_file.name, samplerate, audio)
    return temp_file.name

def transcribe_audio(audio_data, log_path=LOG_FILE):
    try:
        temp_path = save_temp_wav(audio_data)
        result = model.transcribe(temp_path)
        text = result["text"].strip()
        os.remove(temp_path)

        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] 📝 Transcription: {text}\n")

        # Save to .txt log
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {text}\n")

    except Exception as e:
        print(f"❌ Error during transcription: {e}")

def record_and_transcribe_loop():
    print("🎙️ Starting live transcription... Press Ctrl+C to stop.\n")
    try:
        while True:
            audio = record_audio_blocking()
            transcribe_audio(audio)
    except KeyboardInterrupt:
        print("\n🛑 Transcription stopped by user.")

if __name__ == "__main__":
    record_and_transcribe_loop()
