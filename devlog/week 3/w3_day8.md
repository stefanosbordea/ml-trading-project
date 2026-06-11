Day 7:

Overview:
- Created analyst, its signal events and added the mt o backtesting

Struggles:
- Class structure in python
- Concept of what analyst does
- How to implement analyst in backtesting engine

What/How I learned:
- Python documentation to polish class and object structure
- For now, I started small so that i get the foundation running. Analyst now just compares yesterday's price with today's price and if its long, he goes long. The same with short
- In backtest, i had to understand the concept more deep. Essentially the backtest is a loop where i read what type of note is the last one to be added to the tray and direct it to the person i should or take any actions i have to.
- As the tray moves, notes are added and removed, thats why i have a while loop that works until the tray is closed

What's next:
- Manager