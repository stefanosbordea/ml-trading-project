from data_handler import clock
from load import show_ticker_list
from analyst import Analyst
from manager import Manager
from broker import Broker
import numpy as np
import math 

tray = []

total_return_dict = {}
annual_return_dict = {}
max_drawdown_dict = {}
sharpe_ratio_dict = {}
calmar_ratio_dict = {}

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
    
    #total return
    total_profit = manager.equity_curve[-1]-manager.equity_curve[0]
    total_return = (total_profit/manager.equity_curve[0]) * 100
    total_return_dict[ticker] = total_return
    
    
    #annual return
    years = ((dates[-1]-dates[0]).days)/365
    annual_return_dict[ticker] = ((manager.equity_curve[-1]/manager.equity_curve[0]) ** (1/years)-1) * 100
    

    #max drawdown
    max_drawdown = 0
    max_peak = manager.equity_curve[0]
    for i in range(len(manager.equity_curve)):
        if manager.equity_curve[i] > max_peak:
            max_peak = manager.equity_curve[i]

        drawdown = ((max_peak - manager.equity_curve[i])/max_peak) * 100
        if drawdown> max_drawdown:
            max_drawdown = drawdown
    max_drawdown_dict[ticker] = max_drawdown

    #Sharpe ratio
    rewards = []
   
    for i in range(1,len(manager.equity_curve)):
        reward_difference = ((manager.equity_curve[i] - manager.equity_curve[i-1])/manager.equity_curve[i-1])*100
        rewards.append(reward_difference)

    total_rewards = sum(rewards)
    reward_average = total_rewards/len(rewards)
    v = np.std(rewards)
    
    if ticker in more_liquid:
        sharpe = (reward_average/v)*(math.sqrt(252))
        sharpe_ratio_dict[ticker] = sharpe
    
    else :
        sharpe = (reward_average/v)*(math.sqrt(365))
        sharpe_ratio_dict[ticker] = sharpe
    
    #Calmar ratio
    c = annual_return_dict[ticker]/max_drawdown
    calmar_ratio_dict[ticker] = c

            
    

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



        
        
        
        
        
