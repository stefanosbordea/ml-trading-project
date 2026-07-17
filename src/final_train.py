import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from load import show_ticker_list , data_split
import joblib

x_train,x_cv,x_test,y_train,y_cv,y_test = data_split()

#Combine train and cv sets
x_train_cv = pd.concat([x_train,x_cv],ignore_index=True)
y_train_cv = pd.concat([y_train,y_cv],ignore_index=True)

#Fit scaler
scaler = StandardScaler()
x_train_cv_scaled = scaler.fit_transform(x_train_cv)

#Train model
model = LogisticRegression(max_iter=1000,random_state=42)
model.fit(x_train_cv_scaled,y_train_cv)

joblib.dump(model, "models/logistic_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
