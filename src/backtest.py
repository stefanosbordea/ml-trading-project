from data_handler import clock
from load import show_ticker_list

tray = []

tickers = show_ticker_list()
for ticker in tickers:
    for note in clock(ticker):
        tray.append(note)
        while len(tray) != 0:
            n = tray.pop(0)
            print(n.date)
        
        
