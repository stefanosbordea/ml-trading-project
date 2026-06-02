import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from load import show_ticker_list
from scipy.stats import norm

tickers = show_ticker_list()

for ticker in tickers:
    df = pd.read_parquet(f"data/processed/{ticker}.parquet")

    daily_log_returns = df["Log Return"].dropna()
    log_mean = np.mean(daily_log_returns)
    log_std = np.std(daily_log_returns)

    daily_returns = df["Return"].dropna()
    mean = np.mean(daily_returns)
    sigma = np.std(daily_returns)
    

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize = (12,4))

    axes[0].hist(daily_log_returns, bins = 50, density =True, color = 'Blue', edgecolor='black')
    axes[0].set_title("Log Returns")

    axes[1].hist(daily_returns, bins = 50,density =True, color = 'Pink', edgecolor='black')
    axes[1].set_title("Returns")

    for ax in axes:
        ax.set_xlabel("Returns")
        ax.set_ylabel("Density")
    
    log_x = np.linspace(min(daily_log_returns), max(daily_log_returns), 200)
    x= np.linspace(min(daily_returns), max(daily_returns), 200)
    log_y = norm.pdf(log_x,log_mean,log_std)
    y = norm.pdf(x,mean,sigma)

    axes[0].plot(log_x,log_y, color = "red")
    axes[1].plot(x,y, color = "red")

    plt.tight_layout()
    plt.suptitle(ticker)

    plt.savefig(f"data/plots/return_distributions/{ticker}.png")
    plt.close()




