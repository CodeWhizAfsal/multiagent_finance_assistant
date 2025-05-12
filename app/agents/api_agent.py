# app/agents/api_agent.py

import yfinance as yf

def get_asia_tech_exposure(tickers=['TSM', '005930.KS']):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d")
        if len(hist) >= 2:
            change = ((hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100
            data[ticker] = round(change, 2)
    # Mock exposure percentage
    return {
        'aum_percentage': {'today': '22%', 'yesterday': '18%'},
        'changes': data
    }
