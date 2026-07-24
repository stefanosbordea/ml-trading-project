Day 35:

Overview:
- Continued Week 5 with XGBoost
- Learned the concept of boosting vs bagging
- Built an XGBoost classifier and got early stopping working
- Plotted the train vs CV learning curve over boosting rounds
- Result: XGBoost also shows no out-of-sample edge - textbook overfitting

What I learned:
- Bagging (Random Forest) builds trees in parallel and votes; boosting (XGBoost) builds them sequentially, each new tree correcting the previous ensemble's errors (residuals). Trees are weak/shallow; the learning rate scales each one's contribution
- Boosting reduces BIAS (keeps fitting harder patterns) but overfits easily, so it leans on regularization + early stopping
- Early stopping needs a validation set to WATCH - it stops adding trees when CV stops improving. That's why it needs an eval_set, not just training data
- eval_set is a keyword arg holding a LIST of (X, y) tuples (you can monitor multiple sets); order sets the names validation_0, validation_1...
- evals_result() returns a nested dict: validation_0/validation_1 -> {'logloss': [per-round values]}
- My learning curve showed train logloss falling while CV stayed flat at ~0.693 and drifted up - the lines diverge = overfitting. Early stopping picked round 1 as best, meaning the trees add nothing for generalization
- So logistic + Random Forest + XGBoost (linear, bagging, boosting) ALL hit the base rate -> the ceiling is the problem/features, not the model. This closes the "maybe I needed a better model" objection

What's next:
- LightGBM (probably same result - it's XGBoost's cousin), or skip it
- Walk-forward validation, class weights, SHAP
- Write up the Week 5 comparison deliverable: logistic vs RF vs XGBoost, all no out-of-sample edge