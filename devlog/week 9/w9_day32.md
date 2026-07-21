Day 32:

Overview:
- Built the Bollinger band position feature
- Built the volume ratio feature
- Built the calendar day features (one-hot day-of-week) and merged them

What/How I learned:
- Bollinger position = (price - lower) / (upper - lower). 
- Calendar days are categorical, not ordinal (Mon=1..Fri=5 would imply Friday is "5x" Monday), so one-hot dummies
- Can't use get_dummies - it only makes columns for days that appear, so equities would get fewer columns than crypto
- Vectorised comparison: comparing a whole column to one value answers EVERY row at once. No loop, no if - the same thing that caused my "ambiguous truth value" error is what builds the column
- dict.update() merges another dict in - all six calendar columns in one call

What's next:
- Feature count is now 17 + target. Every hardcoded 8 (the :8 slice in data_split and in the analyst) is now wrong, and the saved scaler/model were fitted on 8 columns - all due at the retrain step
- Add the volatility regime indicator (last feature)
- Lookahead audit -> FEATURES.md
- Retrain + re-evaluate
