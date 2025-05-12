# app/agents/analysis_agent.py

from typing import Dict, Any
from openai import OpenAI
import os

# Initialize OpenAI client (ensure your environment variable is set)
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_api_key)


def analyze_data(data: Dict[str, Any], objective: str = "summarize") -> str:
    """
    Analyzes the retrieved data using the specified objective.

    Args:
        data (Dict[str, Any]): The financial data to be analyzed (e.g., text or structured).
        objective (str): Type of analysis. Options: "summarize", "insights", "compare", "risk".

    Returns:
        str: Analysis output from LLM or rule-based logic.
    """

    content = data.get("content", "")
    if not content:
        return "No data provided for analysis."

    prompt = build_prompt(content, objective)

    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial analysis assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=512,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Analysis failed: {str(e)}"


def build_prompt(content: str, objective: str) -> str:
    """
    Builds a prompt based on the analysis objective.
    """
    if objective == "summarize":
        return f"Summarize the following financial data:\n\n{content}"
    elif objective == "insights":
        return f"Extract key financial insights from the following:\n\n{content}"
    elif objective == "compare":
        return f"Compare trends and figures in the following financial data:\n\n{content}"
    elif objective == "risk":
        return f"Identify potential financial risks or red flags in:\n\n{content}"
    else:
        return f"Analyze the following financial content:\n\n{content}"
