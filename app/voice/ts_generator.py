# voice/tts_generator.py

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty('rate', 180)          # Speed of speech (default ~200)
engine.setProperty('volume', 1.0)        # Max volume = 1.0

def speak_text(text: str):
    """
    Converts text to speech using pyttsx3 (offline).

    Args:
        text (str): The text to convert to spoken audio.
    """
    if not text:
        print("No text provided for speech synthesis.")
        return

    engine.say(text)
    engine.runAndWait()
