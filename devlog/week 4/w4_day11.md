Day 11:

Overview:
- Finished first version of Backtesting Engine
- Created an equity curve
- Implemented position tracking 
- Changed comission to 5bps

Struggles:
- Terminology for equity curve,position tracking,bps
- Was not guarding the possibility of spending more money than i have

What/How I learned:
- Positon Tracking - How much of an asset you hold
- Equity curve - equity = cash + position * price , and i get that value over time for every tick
- 1/100th of a percent so 5bps = 0.0005
- I was executing using the same amount of cash for every asset. This is a problem as every asset differs in unit prize. So i changed it to buying specific units rathen than cash

What's next:
- Implement slippage