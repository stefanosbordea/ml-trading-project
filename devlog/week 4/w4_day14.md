Day 14:

Overview:
- Finished total return
- Implemented max drawdown

Struggles:
- Terminology: max drawdown
- Different assets have different time periods so i had to find a way to get that out of every asset
- How to get only the date out of a TimeFrame DataFrame
- Was calculating NaN values on my annual returns

What/How I learned:
- Max drawdown: The drop from the highest peak for each asset
- I just took the dates from each MarketEvent and added them to a dictionary, then subtracted the last entry from the firs tentry to get years
- The problem was I was subtracting DataFrame TimeFrames not an int, so i had to use pd.days() before converting them to years by /365
- My initial raw data included NaN values because some assets did not trade over weekends, so i implemented data_handler.py to drop these NaN values with .dropna() from the raw data


What's next:
- Sharpe ratio