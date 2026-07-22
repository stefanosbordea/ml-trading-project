import pandas as pd

ticker = "TEST"
dates = pd.date_range("2020-01-01", periods=100, freq="B")

test_df = pd.DataFrame({(ticker, "Close"): range(100)}, index=dates)