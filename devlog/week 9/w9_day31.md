Day 31:

Overview:
- Started Phase 2 (Feature Engineering)
- Built the first feature MACD 
- Built a testing dataframe

What/How I learned:
- .ewm(span=N, adjust=False).mean() - calculates a moving weighted average
- MACD - We calculate MACD line(EMA(12)-EMA(26)), then we calculate the signal line(EMA(9) of MACD line).Lastly we calulate their histogram line (macd lien - signal line)
- Used caused lookahead bias because i used .shift(i) and because my range was negative, i was going into the future

What's next:
- Finish features :Bollinger-band position, volume ratio, calendar dummies, volatility regime.
- Finish audit FEATURES.md
