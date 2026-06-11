Day 7:

Overview:
- Started backtesting engine
- Created data handler,events

Struggles:
- Could not understand the idea of the backtesting engine
- Architecture of the backtesting engine

What/How I learned:
- Analogy that helped me understand : The backtesting engine consists of 4 "workers". The clock, the analyst, the manager and the trader. There is a tray that goes through them. First the clock add a note to the tray that says that new market orders are in as well as their prices. Then the analyst looks at previous prices and todays and comes up with a strategy to trade, then he adds a note that says "I will go long". Then the manager sees the note and adds a note that says "okay". Finally the trader executes the trade.

What's next:
- Signals and analyst framework