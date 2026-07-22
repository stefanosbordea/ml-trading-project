Day 33:

Overview:
- Built the volatility regime feature 
- Finished the lookahead audit — walked through every feature and confirmed each looks backward and wrote FEATURES.md
- Ran the full retrain: features.py -> model.py (degree sweep) -> final_train.py -> backtest on the 18-feature model

What I learned:
- Volatility regime = short-run vol / long-run vol (20/60)
- The lookahead audit reduces to one thing: time only enters through .shift(), .rolling(), and .ewm()
- 18 features still show no out-of-sample edge: cv accuracy sits at the base rate, and adding polynomial degree just overfits harder (train ~0.71 while cv dropped). The backtest confirmed it - the model loses to buy-and-hold AND the fixed-20% benchmark on returns, and the couple of Sharpe wins (QQQ, NVDA) are noise

What's next:
- Watch the "Tree ensembles" videos (Course 2 Week 4): sampling with replacement, random forest, XGBoost
- Then Week 5: build Random Forest -> XGBoost -> LightGBM on the same 18 features
- Plus walk-forward validation, class weights, and SHAP