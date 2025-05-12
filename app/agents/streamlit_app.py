# app/streamlit_app.py

import streamlit as st
import requests

st.title("📈 Morning Market Brief")

if st.button("Get Risk Exposure in Asia Tech Stocks"):
    response = requests.get("http://localhost:8000/api/exposure")
    if response.status_code == 200:
        data = response.json()
        st.write(f"AUM Exposure: {data['aum_percentage']['today']} (prev: {data['aum_percentage']['yesterday']})")
        for stock, change in data['changes'].items():
            st.write(f"{stock}: {'🔼' if change > 0 else '🔽'} {change}%")
    else:
        st.error("Failed to fetch market data.")
if st.button("Get Earnings Surprises"):
    response = requests.get("http://localhost:8000/api/earnings")
    if response.status_code == 200:
        st.subheader("Earnings News")
        for stock, headline in response.json().items():
            st.write(f"📰 {stock}: {headline}")
    else:
        st.error("Failed to fetch earnings news.")
from app.agents.retriever_agent import retriever_agent
from pydantic import BaseModel

class QueryInput(BaseModel):
    query: str

@app.post("/api/retrieve")
def retrieve(query_in: QueryInput):
    results = retriever_agent.retrieve(query_in.query)
    return {"results": results}
st.title("📈 Morning Market Brief Generator")

if st.button("🧠 Generate Briefing"):
    exposure = requests.get("http://localhost:8000/api/exposure").json().get("summary", "")
    earnings = requests.get("http://localhost:8000/api/earnings").json()
    retrieval = requests.post("http://localhost:8000/api/retrieve", json={"query": "Asia tech today"}).json().get("results", [])

    input_payload = {
        "exposure": exposure,
        "earnings": earnings,
        "retrieved_info": retrieval
    }

    response = requests.post("http://localhost:8000/api/brief", json=input_payload)
    if response.status_code == 200:
        st.success("📢 Market Brief:")
        st.write(response.json()["brief"])
    else:
        st.error("Failed to generate market brief.")
