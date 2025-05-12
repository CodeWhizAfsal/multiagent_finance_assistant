# app/main.py

from fastapi import FastAPI
from app.agents.api_agent import get_asia_tech_exposure

app = FastAPI()

@app.get("/api/exposure")
def get_exposure():
    return get_asia_tech_exposure()
from app.agents.scraping_agent import get_earnings_summary

@app.get("/api/earnings")
def earnings_summary():
    return get_earnings_summary()
from app.agents.retriever_agent import retriever_agent
from pydantic import BaseModel

class QueryInput(BaseModel):
    query: str

@app.post("/api/retrieve")
def retrieve(query_in: QueryInput):
    results = retriever_agent.retrieve(query_in.query)
    return {"results": results}

from app.agents.language_agent import generate_market_brief
from pydantic import BaseModel

class BriefInput(BaseModel):
    exposure: str
    earnings: dict
    retrieved_info: list

@app.post("/api/brief")
def generate_brief(data: BriefInput):
    result = generate_market_brief(data.exposure, data.earnings, data.retrieved_info)
    return {"brief": result}
