from data_handler import clock
from load import show_ticker_list
from analyst import Analyst
from manager import Manager
from broker import Broker

tray = []

total_return_values = {}
annual_return = {}
max_drawdown_dict = {}


tickers = show_ticker_list()

for ticker in tickers:
    more_liquid = ["SPY","QQQ","AAPL","MSFT","NVDA"]
    less_liquid = ["BTC-USD","ETH-USD"]
    analyst = Analyst()
    manager = Manager(100000)

    dates = []

    if ticker in more_liquid:
        broker = Broker(0.0005,0.0005)
    elif ticker in less_liquid:
        broker = Broker(0.0005,0.001)
    fill = None
    for note in clock(ticker):

        tray.append(note)
        

        while len(tray) != 0:
            n = tray.pop(0)
            

            if (n.event_type == "MARKET"):
                d = n.date
                dates.append(d)

                fill = broker.trade(n)
                if (fill is not None):
                    tray.append(fill)
                signal = analyst.analyze(n)
                if (signal is not None):
                    tray.append(signal)
                    
                    
            elif (n.event_type == "SIGNAL"):
                order = manager.manage(n)
                if (order is not None):
                    tray.append(order)
            
            elif (n.event_type == "ORDER"):
                broker.pending_order(n)
                
            
            elif (n.event_type == "FILL"):
                manager.fill_order(n)
         
               
        equity = manager.mark(note.close)
    
    total_profit = manager.equity_curve[-1]-manager.equity_curve[0]
    total_return = (total_profit/manager.equity_curve[0]) * 100
    years = ((dates[-1]-dates[0]).days)/365
    
    annual_return[ticker] = ((manager.equity_curve[-1]/manager.equity_curve[0]) ** (1/years)-1) * 100
    total_return_values[ticker] = total_return

    max_drawdown = 0
    max_peak = manager.equity_curve[0]
    for i in range(len(manager.equity_curve)):
        if manager.equity_curve[i] > max_peak:
            max_peak = manager.equity_curve[i]

        drawdown = ((max_peak - manager.equity_curve[i])/max_peak) * 100
        if drawdown> max_drawdown:
            max_drawdown = drawdown
    max_drawdown_dict[ticker] = max_drawdown
            
    

"""print()
print("---------------")
print("BACKTEST SUMMARY")
print("Total return:")
for keys,values in total_return_values.items():
    print(f"{keys} = {values}")
for keys, values in annual_return.items():
    print(f"{keys}: {values}")
for keys,values in max_drawdown_dict.items():
    print(f"{keys}: {values}")"""



        
        
        
        
        
