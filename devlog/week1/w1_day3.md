Day 3:

Overview:
- Engineered all features (Return, Log Return, Rolling Volatility (20 and 60 days))
- Created DataFrame with all features for each ticker
- Saved data as a praguet file in data/processed/

Struggles:
- Return, Log Return, Rolling Volatility calculation forumlas
- Was saving features as rows instead of columns in DataFrame
- How to use standard deviation and annualization

What/How I learned:
- Return = (Price-Price day before)/ Price day before
- Log Return = ln(Price/Price day before) 
- Rolling Volatility = used np.rolling() from numpy
- Annualization = multplying the sqrt of a full trading calendar * sqrt(252)

What's Next:
- Plot: price series, return distributions, autocorrelation of returns and squared returns.