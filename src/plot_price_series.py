import matplotlib.pyplot as plt
import pandas as pd
from load import show_ticker_list

tickers = show_ticker_list()

for ticker in tickers:
    df = pd.read_parquet(f"data/raw/{ticker}.parquet")
    date_axis = df.index
    price_axis = df[f"{ticker}"]["Close"]
    plt.plot(date_axis,price_axis)
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title(f"Closing Price for the Past 10 years ({ticker})")
    plt.savefig(f"data/plots/price_series/{ticker}.png")
    plt.close()




