# app/agents/voice_agent.py

import whisper
import pyttsx3

# Initialize Whisper model
whisper_model = whisper.load_model("base")

# Initialize pyttsx3 for TTS
engine = pyttsx3.init()

def speech_to_text(audio_file: str):
    """
    Convert speech to text using Whisper.
    """
    result = whisper_model.transcribe(audio_file)
    return result['text']

def text_to_speech(text: str):
    """
    Convert text to speech using pyttsx3.
    """
    engine.say(text)
    engine.runAndWait()

def save_audio_file(file_path: str):
    """
    Save the audio file to a given path (for testing purposes).
    """
    engine.save_to_file(text, file_path)
    engine.runAndWait()
