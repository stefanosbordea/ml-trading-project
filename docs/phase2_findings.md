# Phase 2 — Findings

## Summary

In phase 2, more features were engineered and these were tested on three different models. After a deeper evaluation than phase 1, the result for every model was negative again. No model gets an out-of-sample edge on next-day direction. This means that to get an edge we will have to gather new information or change the problem formulation, not the model.

## Goal

- Engineer more features , to test whether they can give us an edge.
- Evaluate in a way that gives us an honest result , not just an impressive looking but meaningless one.

## 1. Feature engineering

- Features grew from 8 to 18. The new features are MACD (histogram), Bollinger-band position, volume ratio, volatility-regime ratio and day of the week dummies (one-hot coded, these explain the large growth in feature numbers)
- Made a lookahead audit in `FEATURES.md` . This makes sure that all features take information from the past not the future, the only deliberate forward-looking are the targets.
- Made sure several features are ratios. This way they are unitless. By doing this they are comparable across pooled tickers.

## 2. Models tested
- Logistic regression (linear) 
- Random Forest (bagging) 
- XGBoost (boosting) 
- Result: all three land at the base rate.

| Model | Family | CV accuracy | Edge over base |
|-------|--------|-------------|----------------|
| Base rate (always up) | — | 0.5215 | 0.0000 |
| Logistic Regression | Linear | 0.5268 | +0.0053 |
| Random Forest | Bagging | 0.5075 | −0.0140 |
| XGBoost | Boosting | 0.5162 | −0.0053 |

## 3. Evaluation rigour

- Walk-forward validation - used rolling windows for training and testing. Accuracy is similar to each window's base rate. No edge
- Bootstrapped Sharpe CIs - for every ticker, their 95% CI includes 0.
- SHAP - the model utilizes mostly on return and momentum features. However, there isn't a directional relationship between features and direction. Just because they are the most important, does not mean they produce a signal
- Multi metric - Accuracy,f1,auc were used. F1 looks moderate only because  'up' is the majority class. AUC comes around at 0.50 , therefore no edge.
- Per asset generalization -  Accuracy is at or below its base rate and auc for every asset , therefore it fails all the time.
- Class weights — no effect. The mild imbalance was never the limiting factor.

## 4. Conclusion & next

- The evaluation worked since every method agreed. This makes the negative result credible
- There was still no edge . Nothing produced an out-of-sample signal.
- Next-day direction is currently unpredictable from our current features. Adding more price/volume related features just increased overfitting.
- Moving forward a deep-learning model will be used for phase 3. As a reference, the baseline model used to compare will be XGBoost.