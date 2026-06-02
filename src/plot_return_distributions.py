import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from load import show_ticker_list
from scipy.stats import norm
from scipy.stats import probplot

tickers = show_ticker_list()

for ticker in tickers:
    df = pd.read_parquet(f"data/processed/{ticker}.parquet")

    daily_log_returns = df["Log Return"].dropna()
    log_mean = np.mean(daily_log_returns)
    log_std = np.std(daily_log_returns)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize = (12,4))

      
    log_x = np.linspace(min(daily_log_returns), max(daily_log_returns), 200)
    log_y = norm.pdf(log_x,log_mean,log_std)
    


    axes[0].hist(daily_log_returns, bins = 50, density =True, color = 'Blue', edgecolor='black')
    axes[0].set_title("Log Returns")

    probplot(daily_log_returns, dist= "norm",plot=axes[1])
    axes[1].set_title("QQ")

    axes[0].set_xlabel("Returns")
    axes[0].set_ylabel("Density")
    axes[1].set_xlabel("Theoretical Quantiles")
    axes[1].set_ylabel("Sample Quantiles")
  
    axes[0].plot(log_x,log_y, color = "red")

    plt.tight_layout()
    plt.suptitle(ticker)

    plt.savefig(f"data/plots/return_distributions/{ticker}.png")
    plt.close()




