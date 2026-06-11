from data_handler import clock
from load import show_ticker_list
from analyst import Analyst

tray = []

tickers = show_ticker_list()

for ticker in tickers:
    analyst = Analyst()
    for note in clock(ticker):
        tray.append(note)

        while len(tray) != 0:
            n = tray.pop(0)

            if (n.event_type == "MARKET"):
                signal = analyst.analyze(n)
                if (signal is not None):
                    tray.append(signal)
                    
            elif (n.event_type == "SIGNAL"):
                print(n.date)

        
        
