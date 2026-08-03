from load import show_ticker_list
import pandas as pd
import joblib
from sklearn.metrics import f1_score, roc_auc_score

tickers = show_ticker_list()
generalization_dicts = []
for ticker in tickers:
    df = pd.read_parquet(f"data/processed/{ticker}.parquet")
    index = int(len(df)*0.8)
    df = df[index:]

    x = df.iloc[:,:18]
    y = df.iloc[:,-1]


    model = joblib.load("models/logistic_model.pkl")
    scaler = joblib.load("models/scaler.pkl")

    x_scaled = scaler.transform(x)
    probs = model.predict_proba(x_scaled)[:,1]

    y_pred = model.predict(x_scaled)
    accuracy = model.score(x_scaled,y)
    f1 = f1_score(y,y_pred)
    auc = roc_auc_score(y,probs)

    generalization_dicts.append({"ticker":ticker,"base_rate":y.mean(),"accuracy":accuracy,"f1":f1,"auc":auc})

generalization_df = pd.DataFrame(generalization_dicts)
print(generalization_df.round(3))

