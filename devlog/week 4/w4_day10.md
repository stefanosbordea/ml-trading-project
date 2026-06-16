Day 10:

Overview:
- Created Broker feature and started implementing it into backtesting

Struggles:
- Concept of what broker does
- How to implement analyst in backtesting engine

What/How I learned:
- The broker executes the trade. What i did not undesrtand is that i though the trade was executed at real time with real money. However it just executes the trade on a simulation

What's next:
- I still need to figure out how to implement the fill order on manager.py. 2 struggles : more money is being spent than what i have in the account, bug with the signal (signals always alternate from 100/0 when theyre supposed to be consecutive sometimes)