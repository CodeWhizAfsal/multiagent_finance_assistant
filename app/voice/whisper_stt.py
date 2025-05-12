# voice/whisper_stt.py

import whisper
import os

# Load the model (consider using 'base' or 'small' for faster performance)
model = whisper.load_model("base")

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes speech from an audio file using OpenAI Whisper.

    Args:
        file_path (str): Path to the audio file (WAV/MP3/MP4/M4A).

    Returns:
        str: Transcribed text.
    """
    if not os.path.exists(file_path):
        return "Audio file not found."

    result = model.transcribe(file_path)
    return result.get("text", "")
