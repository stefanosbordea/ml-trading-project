from load import show_ticker_list
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression


def run_walk_forward(model,scaling):
    tickers = show_ticker_list()
    concat_df_list = []

    for ticker in tickers:
        df = pd.read_parquet(f"data/processed/{ticker}.parquet")
        concat_df_list.append(df)
    concat_df = pd.concat(concat_df_list,ignore_index=False).sort_index()

    stop = concat_df.index.max()
    start = concat_df.index.min()

    accuracy = []
    base = []
    while start <= stop-pd.DateOffset(months = 24):   
        training_stop = start + pd.DateOffset(months= 18)
        testing_start = training_stop + pd.DateOffset(days=1)
        training_window = concat_df.loc[start:training_stop]
        testing_stop = testing_start + pd.DateOffset(months=6)
        testing_window = concat_df.loc[testing_start:testing_stop]

        # train model here
        
        x_train= training_window.iloc[:,:18]
        y_train=training_window.iloc[:,-1]
        x_test = testing_window.iloc[:,:18]
        y_test = testing_window.iloc[:,-1]

        if scaling == True:
            scaler = StandardScaler()
            x_train_mapped = scaler.fit_transform(x_train)
            x_test_mapped = scaler.transform(x_test)
        else:
            x_train_mapped = x_train
            x_test_mapped = x_test

        train_model = model
        train_model.fit(x_train_mapped,y_train)
    
        #test model here
        y_pred = train_model.predict(x_test_mapped)
        acc = accuracy_score(y_test,y_pred)
        accuracy.append(acc)
        b = y_test.mean()
        base.append(b)

        start = testing_stop

    plt.plot(accuracy,label = "Accuracy")
    plt.plot(base,label = "Base")
    plt.ylabel("Accuracy/Base")
    plt.xlabel("Window index")
    plt.grid()
    plt.legend()
    plt.show()

run_walk_forward(XGBClassifier(n_estimators = 500, learning_rate = 0.1,verbosity =1,random_state = 55),scaling = False)

        

    