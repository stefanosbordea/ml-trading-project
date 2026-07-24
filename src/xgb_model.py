from load import data_split
from xgboost import XGBClassifier
import matplotlib.pyplot as plt

x_train,x_cv,x_test,y_train,y_cv,y_test = data_split()

xgb_model = XGBClassifier(n_estimators = 500, learning_rate = 0.1, early_stopping_rounds = 10,verbosity =1,random_state = 55)
xgb_model.fit(x_train,y_train,eval_set = [(x_train,y_train),(x_cv,y_cv)])

results = xgb_model.evals_result()
train_results = results["validation_0"]["logloss"]
cv_results = results["validation_1"]["logloss"]

plt.plot(train_results, label = "Train")
plt.plot(cv_results, label = "CV")
plt.xlabel("Boosting round")
plt.ylabel("Loss")
plt.legend()
plt.show()

