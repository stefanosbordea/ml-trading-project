Day 13:

Overview:
- implemented total return
- Started implementing annual return

Struggles:
- Terminology: annual return
- Was just dividing my total return by years which is not correct
- was hardcoding for 10 years when not all asset's raw data are from 10 years

What/How I learned:
- Annual return is ((final equity/initial equity) ** (1/n)-1) * 100 --> where n is the amount of time
- Need to find a way to get a duration of years for each asset


What's next:
- Finish annual return implementation : find a way to get each asset's raw data time period. Since MarketEvent already passes dates, i can add a mechanism like the equity curve but for dates
- Implement max drawdown