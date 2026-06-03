import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from features import show_ticker_list

tickers = show_ticker_list()

for ticker in tickers:
    df = pd.read_parquet(f"data/processed/{ticker}.parquet")
    daily_log_returns = df["Log Return"].dropna()
    squared_returns = (daily_log_returns)**2
    sm.graphics.tsa.plot_acf(squared_returns,lags = 40, title = f"{ticker}")
    
    plt.savefig(f"data/plots/squared_autocorrelation/{ticker}.png")
    plt.close()