import pandas as pd
import numpy as np
from load import read_ticker
from load import show_ticker_list
from testingdf import test_df

def returns(ticker,df):
    close_price = df[f"{ticker}"]["Close"]
    daily_return =(close_price - close_price.shift(1)) / close_price.shift(1)
    return_series = pd.Series(daily_return)
    return return_series

def log_returns(ticker,df):
    close_price = df[f"{ticker}"]["Close"]
    log_return = np.log(close_price/close_price.shift(1))
    log_return_series = pd.Series(log_return)
    return log_return_series

def rol_vol(ticker,df,rolling_period):
    close_price = df[f"{ticker}"]["Close"]
    log_return = np.log(close_price/close_price.shift(1))
    vol =(log_return.rolling(window = rolling_period).std())*np.sqrt(252)
    return vol

def lag_returns(ticker,df,lag_period):
    lag_row = returns(ticker,df).shift(lag_period)
    return lag_row

def run_rsi(ticker,df):
    close_price = df[f"{ticker}"]["Close"]
    daily_return =(close_price - close_price.shift(1)) / close_price.shift(1)

    gains = daily_return.clip(lower=0).rolling(window = 14).mean()
    losses = abs(daily_return.clip(upper=0)).rolling(window = 14).mean()

    rs = gains/losses
    rsi = 100 - (100/(1+rs))
    return rsi

def target(ticker,df):
    current_day_close = df[f"{ticker}"]["Close"]
    next_day_close = current_day_close.shift(-1)
    target_column = (next_day_close>current_day_close).astype(int)
    target_column = target_column.iloc[:-1]
    return target_column

def run_macd(ticker,df):
    current_day_close = df[f"{ticker}"]["Close"]
    
    avg_12 = current_day_close.ewm(span = 12, adjust=False).mean()
    avg_26 = current_day_close.ewm(span = 26, adjust=False).mean()

    macd_line = avg_12 - avg_26
    signal_line = macd_line.ewm(span = 9, adjust=False).mean()
    histogram_line = macd_line - signal_line


    return histogram_line


tickers = show_ticker_list()

for ticker in tickers:
    ticker_dict = {}
    df=read_ticker(ticker)

    daily_return = returns(ticker,df)
    ticker_dict["Return"] = daily_return

    log_return = log_returns(ticker,df)
    ticker_dict["Log Return"] = log_return
    
    vol_20 = rol_vol(ticker,df,20)
    ticker_dict["Rolling Volatility (20 days)"] = vol_20

    vol_60 = rol_vol(ticker,df,60)
    ticker_dict["Rolling Volatility (60 days)"] = vol_60

    lag_1 = lag_returns(ticker,df,1)
    ticker_dict["Lagged Returns (1 day)"] = lag_1
    
    lag_5 = lag_returns(ticker,df,5)
    ticker_dict["Lagged Returns (5 days)"] = lag_5

    lag_10 = lag_returns(ticker,df,10)
    ticker_dict["Lagged Returns (10 days)"] = lag_10
    
    rsi = run_rsi(ticker,df)
    ticker_dict["RSI"] = rsi

    macd = run_macd(ticker,df)
    ticker_dict["MACD"] = macd

    target_column = target(ticker,df)
    ticker_dict["target"] = target_column
   
    ticker_features = pd.DataFrame.from_dict(ticker_dict).dropna()
    ticker_features["target"] = ticker_features["target"].astype(int)
    ticker_features.to_parquet(f"data/processed/{ticker}.parquet")


    



