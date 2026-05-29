import pandas as pd
from load import read_ticker
from load import show_ticker_list

#MAKE A SERIES FOR EACH TICKER WITH ALL FEATURES

returns = pd.DataFrame()

tickers = show_ticker_list()
for ticker in tickers:
    df=read_ticker(ticker)
    daily_return =(df[f"{ticker}"]["Close"] - df[f"{ticker}"]["Close"].shift(1)) / df[f"{ticker}"]["Close"].shift(1)
    return_series = pd.Series(daily_return)
    
#print(daily_return)


