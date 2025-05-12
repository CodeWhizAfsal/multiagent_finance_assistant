# app/agents/language_agent.py

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_market_brief(exposure: str, earnings: dict, retrieval_chunks: list):
    earnings_str = "\n".join([f"{k}: {v}" for k, v in earnings.items()])
    retrieved_info = "\n".join(retrieval_chunks)

    prompt = f"""
You are a financial assistant. Your job is to deliver a concise morning briefing.

Portfolio Exposure:
{exposure}

Earnings Surprises:
{earnings_str}

Market Intel:
{retrieved_info}

Based on this, generate a spoken-style market briefing for a portfolio manager.
Keep it short and insightful.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4
        messages=[
            {"role": "system", "content": "You are a financial assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6
    )

    return response['choices'][0]['message']['content']
