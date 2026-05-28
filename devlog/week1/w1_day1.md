Day 1:

Overview:
- Created git repository and folders required for its structure
- Downloaded data from yfinance, and stored them in parquet files

Struggles:
- Was downloading tickers in batches which led to NaN values in DataFrame
- Didn't know what parquet files were and how to store them separately for each ticker(Stock)

What/How I learned:
- Had to use .to_parquet() in the loop
- Read yfinance documentation to understand how to download data
- Read pyarrow and pandas documentation to learn to manipulate dataframes

What's Next:
- Compute returns, log returns, rolling volatility (20-day, 60-day).
- Plot: price series, return distributions, autocorrelation of returns and squared returns.

