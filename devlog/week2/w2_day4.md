Day 4:

Overview:
- Created .py file that creates price_series plots
- Created plots as png in data/plots/price_series

Struggles:
- Didn't know how to save the plots where i wanted to
- Couldn't access data from DataFrame because i didn't understand its structure

What/How I learned:
- Use plt.savefig() to save plots in any file type (used .png)
- My DataFrame is multi-index so i had to call df.[(ticker)]["Close"] to get closing prices

What's Next:
- Create plots for return distributions, autocorrelation of returns and squared returns.