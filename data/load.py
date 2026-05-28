import yfinance as yf
import pandas as pd

tickerStrings = ["SPY","QQQ","AAPL","MSFT","NVDA","BTC-USD","ETH-USD"]

df_list= []
for ticker in tickerStrings:
    data = yf.download(ticker, group_by = "Ticker", period ="10y")
    data['ticker'] = ticker
    data.to_parquet(f"data/raw/{ticker}.parquet")
    

