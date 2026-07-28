import numpy as np
import pandas as pd
from load import show_ticker_list
import math
from backtest import run_backtest

def calculate_sharpe(rewards,period):

    total_rewards = sum(rewards)
    reward_average = total_rewards/len(rewards)
    v = np.std(rewards)
    
    sharpe = (reward_average/v)*(math.sqrt(period))

    return sharpe

tickers = show_ticker_list()
more_liquid = ["SPY","QQQ","AAPL","MSFT","NVDA"]
less_liquid = ["BTC-USD","ETH-USD"]

records = []
for ticker in tickers:
    curve,dates = run_backtest(ticker,"simple logistic")

    rewards=[]
    for i in range(1,len(curve)):
        reward_difference = ((curve[i] - curve[i-1])/curve[i-1])*100
        rewards.append(reward_difference)
        
    period =252 if ticker in more_liquid else 365

    point_sharpe = calculate_sharpe(rewards,252)

    boot_sharpes=[]
    for i in range(10000):
        rndm = np.random.choice(rewards, size=len(rewards), replace= True)
        boot_sharpes.append(calculate_sharpe(rndm,period))

    low,high = np.percentile(boot_sharpes, [2.5,97.5])

    records.append({"ticker":ticker,"sharpe": point_sharpe, "ci_low": low, "ci_high": high})

df = pd.DataFrame(records)
print(df.round(3))

        

        





    