from data_handler import clock
from load import show_ticker_list
from analyst import Analyst
from manager import Manager
from broker import Broker

tray = []

tickers = show_ticker_list()

for ticker in tickers:
    analyst = Analyst()
    manager = Manager(100000)
    broker = Broker(10)
    fill = None
    for note in clock(ticker):
        tray.append(note)

        while len(tray) != 0:
            n = tray.pop(0)

            if (n.event_type == "MARKET"):
                fill = broker.trade(n)
                if (fill is not None):
                    tray.append(fill)
                signal = analyst.analyze(n)
                if (signal is not None):
                    tray.append(signal)
                    print(signal)
                else:
                    print("None")
                    
            elif (n.event_type == "SIGNAL"):
                order = manager.manage(n)
                if (order is not None):
                    tray.append(order)
            
            elif (n.event_type == "ORDER"):
                broker.pending_order(n)
                
            
            elif (n.event_type == "FILL"):
                manager.fill_order(n)
               
       

        
        
