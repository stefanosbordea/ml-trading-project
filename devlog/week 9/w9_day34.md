Day 34:

Overview:
- Built a Random Forest hyperparameter sweep (min_samples_split, max_depth, n_estimators) with sklearn
- Modularized it into generic build/plot functions using ** dict unpacking
- Result: Random Forest shows no out-of-sample edge either - decided not to backtest it, but will note in the deliverable that it was tested

What I learned:
- Random forest = single-tree machinery + two new pieces: sampling with replacement (bagging) wraps AROUND build_tree (each tree gets its own bootstrap sample), and a random feature subset goes INSIDE best_split. Then a loop of N trees + majority vote on top
- Trees are scale-invariant (they split on thresholds), so unlike logistic they need NO scaler - I correctly fed raw features
- ** dict unpacking: to set a keyword argument whose NAME is decided at runtime, build a {name: value} dict and unpack it into the call. Plain `name = value` can't do it because the left side of `=` is taken literally, not evaluated
- All three RF sweeps: train swings up to ~1.0 (memorizing) but validation stays flat at ~0.50-0.53 (base rate) at EVERY setting. No config beats baseline
- So a flexible nonlinear ensemble ALSO finds no edge -> strong evidence the ceiling is the problem/features, not the model class

What's next:
- XGBoost on the same 18 features, then LightGBM
- Walk-forward validation, class weights, SHAP
- Write up in the Week 5 deliverable that RF was tested and showed no out-of-sample edge (not added to backtest)
