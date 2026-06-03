import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula as smf
from features import show_ticker_list

tickers = show_ticker_list()

for ticker in tickers:
    df = pd.read_parquet(f"data/processed/{ticker}.parquet")

    daily_log_returns = df["Log Return"].dropna()
    sm.graphics.tsa.plot_acf(daily_log_returns,lags = 40, title = f"{ticker}")
    
    plt.savefig(f"data/plots/autocorrelation/{ticker}.png")
    plt.close()



