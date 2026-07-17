Day 28:

Overview:
- Built the ML analyst method (simple_logistic_regression)
- Loaded model + scaler once, look up feature row per bar, scale, predict, emit signal
- Wired "simple logistic" into run_backtest dispatch + results dict
- Started the test-window slice for honest evaluation

What/How I learned:
- Used loc[[date]] to keep the row 2D, then iloc[:,:8] to drop target and keep 8 features
- Learned sklearn needs a (1,8) table not a flat (8,) list
- Used transform (not fit_transform) at inference so I reuse the saved scaler, no leak
- Cached the parquet with an "is None" guard so it loads once, not every bar
- predict returns an array so I check y_pred[0]
- Realized running the model over full history is a memory test, not out-of-sample - only score the last 20% (test window), but still run over everything so SMA/12-1 warm up
- Multiplying the curve by 0.2 scales dollars, doesn't slice time - need to slice the last 20% of entries instead

What's next:
- Finish the test-window slice (80% index = int(len(curve)*0.8)), apply to all strategies
- Build the comparison table + honest writeup (close Phase 1)
- Then Phase 2: add new features