Day 30:

Overview:
- Built the always-20%-long benchmark (new analyst method + Manager sizing + dispatch)
- Ran it - the clean same-exposure test of whether the model's timing adds anything
- Refactored backtest.py output into a tidy DataFrame + pretty tables with tabulate
- Wrote the results to a markdown report file (per-metric tables)

What/How I learned:
- The benchmark answered the real question: the ML makes LESS return than just being 20% long on every rising asset (SPY, QQQ, AAPL, NVDA) - its timing costs return
- It only "wins" on assets that fell (MSFT, ETH) where stepping aside dodged losses - that's a de-risking overlay, not directional skill
- So against a fair same-exposure benchmark the model shows no reliable edge - stronger evidence than "beats buy-and-hold on Sharpe"
- Used tabulate (headers="keys", tablefmt="github", floatfmt=".2f") for clean markdown/ASCII tables
- Tidy DataFrame (one row per ticker+strategy) then pivot per metric = readable comparison tables
- tabulate returns a string, so I can write it to a .md file with open(...,"w")
- Bugs I caught: pivot result has to be assigned or it's discarded; results_table was overwriting each loop instead of accumulating (+=); metric names must match the run_metrics keys exactly (underscores); tabulate output has no trailing newline so sections glue together without "\n\n"

What's next:
- Add a statistical significance test (bootstrapped Sharpe confidence intervals) to confirm the "no edge" result isn't noise
- Fix the BTC never-trades bug for the rule-based strategies
- Phase 2: richer features (MACD, Bollinger, volume, calendar) + tree models (RF, XGBoost, LightGBM)