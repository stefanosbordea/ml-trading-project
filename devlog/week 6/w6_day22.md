Day 22:

Overview:
- Implemented lag returns
- Implemented rsi
- Implemented target output

Struggles:
- Terminology: lag return, rsi
- Did not know how to shift from one row of a Dataframe to the other
- How to compare if a series is positive or negative without if condition
- How to cast series

What/How I learned:
- Lag return - The return before a certain period of time
- RSI - ratio of total gain against total losses
- .shift(+n) for past values, shift(-n) for future values
- .clip(lower=0) all negative values become 0,.clip(upper=0) all positive values become 0 / use .abs() to turn negative values into positive
- pd.astype(int) to cast Series into int

What's next:
- Train logistic regression model
