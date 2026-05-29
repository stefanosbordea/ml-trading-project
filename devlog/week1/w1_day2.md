Day 2:

Overview:
- Found a way, using data frames, to combine all features together to train the model
- I worked on the 'returns' feature
- Then realized that its better to do all features per ticker then move on to the next ticker
- Worked on the return feature of the SPY ticker

Struggles:
- Did not know how to calculate return value
- Did not know how to manipulate and read DataFrames
- Did not have a src folder
- Did not know how to import code from one file to another
- Had to change my strategy from working by feature, to working by ticker

What/How I learned:
- Had to search what a return value is in trading and found its formula
- Had to read pandas documentation to learn how to manipulate DataFrames and Series
- Learned that there is almost a data,backtest,notebooks,models,src and test folder system in programms (or similar)
- Learned to use "from file import code"
- Its better to work by ticker and complete all its features, so that i can create a DataFrame for each ticker and use them as training sets

What's Next:
- Finish creating DataFrames for each ticker. Features include :return, log return, rolling vollatility (20-day, 60-day)
- Plot: price series, return distributions, autocorrelation of returns and squared returns.

