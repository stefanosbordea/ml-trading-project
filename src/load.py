import yfinance as yf
import pandas as pd

def show_ticker_list():
    tickerStrings = ["SPY","QQQ","AAPL","MSFT","NVDA","BTC-USD","ETH-USD"]
    return tickerStrings

def download_ticker(ticker):
    data = yf.download(ticker, group_by = "Ticker", period ="10y")
    data['ticker'] = ticker
    return data

def read_ticker(t):
    df = pd.read_parquet(f"data/raw/{t}.parquet")
    return df



tickers = show_ticker_list()
for ticker in tickers:
    data = download_ticker(ticker)
    data.to_parquet(f"data/raw/{ticker}.parquet")
    

