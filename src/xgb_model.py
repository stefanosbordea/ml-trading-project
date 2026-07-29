from load import data_split
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import shap
from sklearn.metrics import f1_score

def run_shap_plot(model,x_test):
    xgb_explainer = shap.TreeExplainer(model)
    values = xgb_explainer.shap_values(x_test)
    shap.summary_plot(values,x_test)

def run_plot_validation(model):
    results = model.evals_result()
    train_results = results["validation_0"]["logloss"]
    cv_results = results["validation_1"]["logloss"]

    plt.plot(train_results, label = "Train")
    plt.plot(cv_results, label = "CV")
    plt.xlabel("Boosting round")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()

x_train,x_cv,x_test,y_train,y_cv,y_test = data_split()

xgb_model = XGBClassifier(n_estimators = 500, learning_rate = 0.1, early_stopping_rounds = 10,verbosity =1,random_state = 55, scale_pos_weight = 0.85)
xgb_model.fit(x_train,y_train,eval_set = [(x_train,y_train),(x_cv,y_cv)])

run_plot_validation(xgb_model)





