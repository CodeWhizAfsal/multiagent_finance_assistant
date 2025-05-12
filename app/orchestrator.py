# app/orchestrator.py

from fastapi import FastAPI
from pydantic import BaseModel
import requests
from app.agents.voice_agent import speech_to_text, text_to_speech
from app.agents.retriever_agent import retriever_agent
from app.agents.language_agent import generate_market_brief

app = FastAPI()

class VoiceInput(BaseModel):
    audio_file: str

class TextInput(BaseModel):
    query: str

@app.post("/api/orchestrate-speech-to-text")
def orchestrate_stt(voice_input: VoiceInput):
    # Convert speech to text
    transcription = speech_to_text(voice_input.audio_file)
    return {"transcription": transcription}

@app.post("/api/orchestrate-query")
def orchestrate_query(query_in: TextInput):
    # Retrieve info using retriever agent
    retrieval = retriever_agent.retrieve(query_in.query)
    
    # Generate market brief using language agent
    exposure = "Your current exposure is 22%"  # Replace with actual data
    earnings = {"TSMC": "beat estimates by 4%", "Samsung": "missed by 2%"}
    market_brief = generate_market_brief(exposure, earnings, retrieval)

    # Convert generated text to speech
    text_to_speech(market_brief)

    return {"market_brief": market_brief}
