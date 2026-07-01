import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from load import show_ticker_list



#Splitting data 60/20/20
tickers = show_ticker_list()
x_train_list = []
x_cv_list = []
x_test_list = []
y_train_list = []
y_cv_list = []
y_test_list = []

for ticker in tickers :
    df = pd.read_parquet(f"data/processed/{ticker}.parquet")
    x = df.iloc[:,:8]
    y = df.iloc[:,-1]

    x_tr,x_,y_tr,y_ = train_test_split(x,y, test_size = 0.40, shuffle = False)
    x_var,x_te,y_var,y_te = train_test_split(x_,y_, test_size = 0.50, shuffle = False )
    x_train_list.append(x_tr)
    x_cv_list.append(x_var)
    x_test_list.append(x_te)
    y_train_list.append(y_tr)
    y_cv_list.append(y_var)
    y_test_list.append(y_te)

x_train = pd.concat(x_train_list, ignore_index = True)
x_cv = pd.concat(x_cv_list, ignore_index= True)
x_test = pd.concat(x_test_list,ignore_index=True)
y_train = pd.concat(y_train_list,ignore_index=True)
y_cv = pd.concat(y_cv_list,ignore_index=True)
y_test = pd.concat(y_test_list,ignore_index=True)

#Scaling data
scaler_linear = StandardScaler()

x_train_scaled = scaler_linear.fit_transform(x_train)
x_cv_scaled = scaler_linear.transform(x_cv)
x_test_scaled = scaler_linear.transform(x_test)

#Fitting model
model = LogisticRegression()
model.fit(x_train_scaled,y_train)

y_pred = model.predict(x_train_scaled)
print(y_train.mean())
print("Accuracy on training set:", model.score(x_train_scaled,y_train))
print("Accuracy on the cv test:", model.score(x_cv_scaled,y_cv))
print(y_cv.mean())





