Day 15:

Overview:
- Finished Sharpe and Calmar ratio

Struggles:
- Terminology: Sharpe ratio, Calmar ratio

Sharpe:
- Numerator struggles - I was using the first and last values of the equity curve 
- Annualizng the ratio - I was dividing by 252 

Calmar:
- Over engineering - I was using for loops through the dictionaries 

What/How I learned:
Both are risk-reward measurments:
- Sharpe ratio - The average return over the volatillity
- Calmar ratio - Annualized return over max drawdown

Sharpe:
- Use bar to bar percentage changes instead of equity
- Annualize by  multiplying by sqrt(252)

Calmar:
- Get the calmar ratio values just by using the variables in the for loop i am currently in

What's next:
- Running buy-and-hold