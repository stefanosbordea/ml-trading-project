import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from load import show_ticker_list , data_split


x_train,x_cv,x_test,y_train,y_cv,y_test = data_split()

train_bases = []
cv_bases = []
train_scores = []
cv_scores = []
models = []
polys =[]
scalers = []

for degree in range(1,5):
    #Polynomial features
    poly = PolynomialFeatures(degree, include_bias = False)
    x_train_mapped = poly.fit_transform(x_train)
    polys.append(poly)

    #Scaling data
    scaler_poly = StandardScaler()
    x_train_mapped_scaled = scaler_poly.fit_transform(x_train_mapped)
    scalers.append(scaler_poly)


    #Fitting model
    model= LogisticRegression(max_iter=1000, random_state=42)
    model.fit(x_train_mapped_scaled,y_train)
    models.append(model)

    #Adding polynomial features and scaling to CVS 
    x_cv_mapped = poly.transform(x_cv)
    x_cv_mapped_scaled = scaler_poly.transform(x_cv_mapped)

    y_pred = model.predict(x_train_mapped_scaled)
    
    train_base = y_train.mean()
    train_score = model.score(x_train_mapped_scaled,y_train)

    cvs_base = y_cv.mean()
    cvs_score = model.score(x_cv_mapped_scaled,y_cv)

    train_bases.append(train_base)
    train_scores.append(train_score)
    cv_bases.append(cvs_base)   
    cv_scores.append(cvs_score)

degrees = range(1,5)
optimal_grade = degrees[np.argmax(cv_scores)]


plt.figure(figsize=(8,5))

plt.subplot(1,2,1)
plt.plot(degrees,train_bases, label = "Train Baseline")
plt.plot(degrees,cv_bases, label = "CV Baseline")
plt.xlabel('Polynomial Degree')
plt.ylabel("Baseline")

plt.subplot(1,2,2)
plt.plot(degrees,train_scores, label = "Train Accuracy")
plt.plot(degrees, cv_scores, label = "CV Accuracy")
plt.xlabel('Polynomial Degree')
plt.ylabel("Accuracy")


plt.title('Baseline/Accuracy vs Polynomial Degree')
plt.legend()

plt.show()






