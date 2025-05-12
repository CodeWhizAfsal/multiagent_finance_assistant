# app/agents/scraping_agent.py

import requests
from bs4 import BeautifulSoup

def get_earnings_summary(tickers=["TSM", "005930.KS"]):
    summaries = {}
    
    for ticker in tickers:
        query = f"{ticker} earnings"
        url = f"https://news.google.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("a", class_="VDXfz", limit=2)

            if not articles:
                summaries[ticker] = "No recent earnings news found."
                continue

            titles = [a.get_text(strip=True) for a in articles]
            summaries[ticker] = titles[0] if titles else "No title found."
        except Exception as e:
            summaries[ticker] = f"Error fetching news: {str(e)}"
    
    return summaries
