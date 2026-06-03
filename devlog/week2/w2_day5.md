Day 5:

Overview:
- Created .py file that plots return distributions and QQ plots
- Created return distribution and qq plots as .png in data/plots/return_distributions

Struggles:
- Terminology: return distribution and qq plots
- Plotting subplots using matplotlib
- Plotting normal distribution curves on histograms and qq plots

What/How I learned:
- Using online finance sources i learned that return distribution plots are histograms of frequency/density and probability
- QQ plots are complementary to return distribution plots and help you read them
- To plot subplots - plt.subplot()
- To plot normal distribution curves :
    Import scipy.stats and np.linspace for return distribution plots
    From scipy.stats import probplot for qq plot

What's next:
- Create plots for autocorrelation of returns and squared returns.