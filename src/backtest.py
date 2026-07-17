from data_handler import clock
from load import show_ticker_list
from analyst import Analyst
from manager import Manager
from broker import Broker
import numpy as np
import math 
def index(curve,dates):
    idx = int(len(dates) * 0.8)
    curve = curve[idx:]
    dates = dates[idx:]
    return curve,dates

def run_backtest(ticker, strategy):
    tray = []

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
                if strategy == "momentum":
                    signal = analyst.analyze(n)
                elif strategy == "buy_and_hold":
                    signal = analyst.buy_and_hold(n)
                elif strategy == "sma":
                    signal = analyst.sma_crossover(n)
                elif strategy == "12-1":
                    signal = analyst.twelve_minus_one(n)
                elif strategy == "simple logistic":
                    signal = analyst.simple_logistic_regression(n)
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

        manager.mark(note.close)

    manager.equity_curve,dates = index(manager.equity_curve,dates)
    return manager.equity_curve,dates

def run_metrics(curve, dates, period_per_year):
    
    #total return
    total_profit = curve[-1]-curve[0]
    total_return = (total_profit/curve[0]) * 100
    
    
    #annual return
    years = ((dates[-1]-dates[0]).days)/365
    annual_return = ((curve[-1]/curve[0]) ** (1/years)-1) * 100

    #max drawdown
    max_drawdown = 0
    max_peak = curve[0]
    for i in range(len(curve)):
        if curve[i] > max_peak:
            max_peak = curve[i]

        drawdown = ((max_peak - curve[i])/max_peak) * 100
        if drawdown> max_drawdown:
            max_drawdown = drawdown

    #Sharpe ratio
    rewards = []
   
    for i in range(1,len(curve)):
        reward_difference = ((curve[i] - curve[i-1])/curve[i-1])*100
        rewards.append(reward_difference)

    total_rewards = sum(rewards)
    reward_average = total_rewards/len(rewards)
    v = np.std(rewards)
    
    sharpe = (reward_average/v)*(math.sqrt(period_per_year))

    
    #Calmar ratio
    calmar = annual_return/max_drawdown
    
    return {"total_return":total_return,"annual_return":annual_return,"max_drawdown":max_drawdown,"sharpe":sharpe,"calmar":calmar}

#Dicitonaries
momentum_results = {}
bah_results = {}
sma_results = {}
twelve_one_results = {}
simple_logistic_results = {}

if __name__ == "__main__":
    tickers = show_ticker_list()

    more_liquid = ["SPY","QQQ","AAPL","MSFT","NVDA"]
    less_liquid = ["BTC-USD","ETH-USD"]

    
    for ticker in tickers:
    
        #Curves
        momentum_curve,dates = run_backtest(ticker,"momentum")  
        bah_curve,dates = run_backtest(ticker,"buy_and_hold")
        sma_curve,dates = run_backtest(ticker,"sma")
        twelve_one_curve,dates = run_backtest(ticker,"12-1")
        simple_logistic_curve,dates = run_backtest(ticker,"simple logistic")
        


        if ticker in more_liquid:
            momentum_results[ticker] = run_metrics(momentum_curve,dates,252)
            bah_results[ticker] = run_metrics(bah_curve,dates,252)
            sma_results[ticker] = run_metrics(sma_curve,dates,252)
            twelve_one_results[ticker] = run_metrics(twelve_one_curve,dates,252)
            simple_logistic_results[ticker] = run_metrics(simple_logistic_curve,dates,252)

        elif ticker in less_liquid:
            momentum_results[ticker] = run_metrics(momentum_curve,dates,365)
            bah_results[ticker] = run_metrics(bah_curve,dates,365)
            sma_results[ticker] = run_metrics(sma_curve,dates,365)
            twelve_one_results[ticker] = run_metrics(twelve_one_curve,dates,365)
            simple_logistic_results[ticker] = run_metrics(simple_logistic_curve,dates,365)

    print(f"| Momentum: {momentum_results} | BAH : {bah_results} | SMA : {sma_results} | 12-1 : {twelve_one_results} | Simple Logistic Regression : {simple_logistic_results}")
            
        
        
        
        
