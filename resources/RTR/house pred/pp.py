import pandas as pd
import datetime
data = pd.read_csv("D:\Github\program-examples\RTR\house pred\Hyderabad.csv")
# print(data)
# data.info()
# data.describe()
# data.isnull()
# data.isnull().sum()
date_time = datetime.datetime.now()
print(date_time)
print(data)
# data["Fuel_Type"].unique()
# data["Fuel_Type"] = data["Fuel_Type"].map({'key1':0, 'key2':1})
X = data.drop(["Location","Area","Price"],axis=1)
Y = data["Price"]
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.20,random_state=42)
print(X_test)
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor

lr = LinearRegression()
lr.fit(X_train,Y_train)
rf = RandomForestRegressor()
rf.fit(X_train,Y_train)
xgb = GradientBoostingRegressor()
xgb.fit(X_train,Y_train)
xg = XGBRegressor()
xg.fit(X_train,Y_train)

y_pred1 = lr.predict(X_test)
y_pred2 = rf.predict(X_test)
y_pred3 = xgb.predict(X_test)
y_pred4 = xg.predict(X_test)

from sklearn import metrics
score1 = metrics.r2_score(Y_test,y_pred1)
score2 = metrics.r2_score(Y_test,y_pred2)
score3 = metrics.r2_score(Y_test,y_pred3)
score4 = metrics.r2_score(Y_test,y_pred4)

print(score1,score2,score3,score4)

rf = RandomForestRegressor()
xg_final = rf.fit(X_train,Y_train)
# xg = XGBRegressor()
# xg_final = xg.fit(X,Y)

import os
import joblib

directory = './model/'
if not os.path.exists(directory):
    os.makedirs(directory)
joblib.dump(xg_final, './model/hyderabad_predictor')
 