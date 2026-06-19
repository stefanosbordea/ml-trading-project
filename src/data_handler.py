import pandas as pd
from events import MarketEvent

def clock(ticker):
    df = pd.read_parquet(f"data/raw/{ticker}.parquet")
    dropped = df.dropna()
    dropped = dropped.droplevel(0, axis=1)
    for i in range(len(dropped)):
        row = dropped.iloc[i]
        note = MarketEvent(
            event_type= "MARKET",
            symbol = ticker,
            date = row.name,
            open = row["Open"],
            high = row["High"],
            low = row["Low"],
            close = row["Close"],
            volume = row["Volume"]
        )
        yield note
