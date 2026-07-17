Day 29:

Overview:
- Finished the test-window slice (run over full history for warm-up, only measure the last 20%)
- Debugged the ML backtest until it produced real numbers
- Ran the full out-of-sample comparison: ML vs momentum/SMA/12-1 vs buy-and-hold
- Added shorting to the ML strategy
- Wrote the 03_backtest_report_2 notebook with the findings

What/How I learned:
- Got a KeyError - early warmup dates exist in the raw data but not in my processed features (I dropna'd them), so I guard the lookup with "if date in self.features.index"
- ML gave all 0s at first because I'd deleted the "return SignalEvent" line - it predicted but never emitted a signal, so it never traded
- My Manager sizing was inverted (LONG->0, SHORT->0.2*equity) so I was trading against the model - flipped it to LONG->0.2*equity, SHORT->0
- On returns the ML loses to buy-and-hold everywhere (expected - the model has ~zero out-of-sample edge)
- ML Sharpe/Calmar looked higher than buy-and-hold on some tickers, but that's from lower exposure and smaller drawdowns, NOT skill - it matches the zero accuracy result and is probably just noise over a short window
- long/flat only tests the model's "up" calls; adding a real short makes it symmetric but my backtester doesn't model short borrow costs so it's slightly optimistic
- Don't add shorts to every strategy - it changes many variables at once and redefines my established baselines (bad science)

What's next:
- Add an always-20%-long benchmark + bootstrapped Sharpe significance test to confirm there's no real edge
- Fix the BTC "never trades" bug for the rule-based strategies
- Phase 2: richer features (MACD, Bollinger, volume ratios, calendar) + tree models (RF, XGBoost, LightGBM)