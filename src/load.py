import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split

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

def data_split():
    #Splitting data 60/20/20
    tickers = show_ticker_list()
    x_train_list = []
    x_cv_list = []
    x_test_list = []
    y_train_list = []
    y_cv_list = []
    y_test_list = []

    for ticker in tickers :
        df = pd.read_parquet(f"data/processed/{ticker}.parquet")
        x = df.iloc[:,:18]
        y = df.iloc[:,-1]

        x_tr,x_,y_tr,y_ = train_test_split(x,y, test_size = 0.40, shuffle = False)
        x_var,x_te,y_var,y_te = train_test_split(x_,y_, test_size = 0.50, shuffle = False )
        x_train_list.append(x_tr)
        x_cv_list.append(x_var)
        x_test_list.append(x_te)
        y_train_list.append(y_tr)
        y_cv_list.append(y_var)
        y_test_list.append(y_te)

    x_train = pd.concat(x_train_list, ignore_index = True)
    x_cv = pd.concat(x_cv_list, ignore_index= True)
    x_test = pd.concat(x_test_list,ignore_index=True)
    y_train = pd.concat(y_train_list,ignore_index=True)
    y_cv = pd.concat(y_cv_list,ignore_index=True)
    y_test = pd.concat(y_test_list,ignore_index=True)

    return x_train,x_cv,x_test,y_train,y_cv,y_test

tickers = show_ticker_list()
for ticker in tickers:
    data = download_ticker(ticker)
    data.to_parquet(f"data/raw/{ticker}.parquet")

    

