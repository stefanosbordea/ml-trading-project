# FEATURES.md

Documentation of the model's input features and the **lookahead-bias audit**.

All features are produced in `src/features.py`, computed per ticker and pooled across the universe (SPY, QQQ, AAPL, MSFT, NVDA, BTC-USD, ETH-USD). Each processed file holds **18 feature columns + 1 target column**.

## Audit rule

A feature is **lookahead-safe** if its value on day *t* uses **only information available at or before the close of day *t***. Nothing dated after *t* may enter.

Time enters this code through exactly three operations — `.shift()`, `.rolling()`, and `.ewm()` — so the audit checks the direction of each:

- **`.shift(N)`** — positive N reaches into the **past** (safe); negative N reaches into the **future** (leak).
- **`.rolling(window=N)`** — trailing by default (current + prior N−1 rows = backward, safe); would only leak with `center=True` (not used).
- **`.ewm(...)`** — weights current and past values only (backward, safe).

Same-row arithmetic (`+`, `-`, `/`, `.clip()`) cannot leak. Using the **current** day's own close/volume is fine — it is known at the close of *t*.

**Result: all 18 features look backward. The only forward-reaching operation in the file is the target's `shift(-1)`, which is intentional and quarantined as the label.**

## Features

| # | Feature | Built from | Window / params | Captures | Lookahead check |
|---|---------|-----------|-----------------|----------|-----------------|
| 1 | Return | Close | `shift(1)` | Daily % price change | `shift(1)` → past. Uses *t* and *t−1*. ✓ |
| 2 | Log Return | Close | `shift(1)` | Daily log price change | Same `shift(1)` → past. ✓ |
| 3 | Rolling Volatility (20d) | Log returns | trailing 20, ×√252 | Short-run volatility level | `shift(1)` + trailing `rolling(20).std()` → both past. ✓ |
| 4 | Rolling Volatility (60d) | Log returns | trailing 60, ×√252 | Long-run volatility level | Same as above, 60-window. ✓ |
| 5 | Lagged Returns (1d) | Return | `shift(1)` on Return | Prior-day return | Return already backward, shifted further back. ✓ |
| 6 | Lagged Returns (5d) | Return | `shift(5)` on Return | Return 5 days ago | Positive shift → past. ✓ |
| 7 | Lagged Returns (10d) | Return | `shift(10)` on Return | Return 10 days ago | Positive shift → past. ✓ |
| 8 | RSI | Close | 14-day | Overbought/oversold momentum | `shift(1)` + two trailing `rolling(14).mean()` → past. ✓ |
| 9 | MACD (histogram) | Close | EMA 12/26, signal EMA 9 | Momentum acceleration | Three `.ewm()` (backward) + same-row subtractions. ✓ |
| 10 | Bollinger position (%B) | Close | 20-day mean ± 2σ | Position within volatility-scaled range | Trailing `rolling(20)` mean/std; current close known at *t*. ✓ |
| 11 | Volume Ratio | Volume | trailing 20 | Participation vs own norm | Trailing `rolling(20).mean()`; today's volume known at *t*. ✓ |
| 12 | is_monday | Date index | `dayofweek == 0` | Calendar / day-of-week | Date is known in advance; no time-op. ✓ |
| 13 | is_tuesday | Date index | `dayofweek == 1` | Calendar / day-of-week | Known in advance. ✓ |
| 14 | is_wednesday | Date index | `dayofweek == 2` | Calendar / day-of-week | Known in advance. ✓ |
| 15 | is_thursday | Date index | `dayofweek == 3` | Calendar / day-of-week | Known in advance. ✓ |
| 16 | is_friday | Date index | `dayofweek == 4` | Calendar / day-of-week | Known in advance. ✓ |
| 17 | is_saturday | Date index | `dayofweek == 5` | Calendar / day-of-week | Known in advance. ✓ |
| 18 | Volatility Regime | Rolling vol 20 & 60 | ratio 20 / 60 | Vol elevated vs baseline | No new time-op; inherits from `rol_vol` (backward). ✓ |

## Target (label — not a feature)

| Target | Built from | Definition | Note |
|--------|-----------|-----------|------|
| target | Close | `(close.shift(-1) > close).astype(int)` | Next-day direction (1 = up, 0 = down) |

The target uses a **negative** shift — it deliberately looks one day into the future, because it is the thing we are predicting. It is safe because:

1. **It is excluded from the features.** Target is the last column (index 18); the feature slice `iloc[:, :18]` stops before it.
2. **The fabricated last row is dropped.** `shift(-1)` leaves the final row with no real "tomorrow," so it is removed (`iloc[:-1]`, plus `dropna` when the frame is built).

## Notes

- **Unitless features pool cleanly.** Bollinger %B, Volume Ratio, and Volatility Regime are ratios, so their units cancel and they are directly comparable across assets — essential because all tickers are pooled into one training set. Raw price levels or raw volume would be meaningless pooled.
- **Scaling is handled at the split, not here.** The `StandardScaler` is fit on the training portion only and applied to CV/test; `features.py` produces raw feature values.
- **Column-name caveats.** The column labeled `MACD` is specifically the **histogram** (macd_line − signal_line), and `Bollinger Bands` is the **%B position ratio**, not the raw bands.
- **Weekend dummies are confounded with asset class.** Only BTC-USD and ETH-USD trade Saturdays/Sundays, so `is_saturday` (and any weekend signal) can only ever be non-zero on crypto rows — its coefficient partly reflects "this is crypto," not a pure weekend effect. Read it with that in mind.
- **Dropped reference category.** Sunday has no column; it is the reference level for the one-hot day-of-week encoding (a Sunday row is all-zero across the six day dummies), avoiding the dummy-variable trap.
