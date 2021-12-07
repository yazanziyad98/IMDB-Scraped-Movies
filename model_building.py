# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:37:22 2021

@author: yazan
"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

df = pd.read_csv('eda_data.csv')
df2 = df.copy()
 

df.columns
df['MPAA Rating'].value_counts()
# get dummy data 
Rating_encoded = pd.get_dummies(df2['MPAA Rating'])
df_final=df2.join(Rating_encoded, rsuffix='1')


abs(df_final.corr()['Rating']).sort_values(ascending=False)
 
label =df_final.Rating


#drp columns that are mostly zeros
df_final.drop(['Gross'],axis=1,inplace=True)

# drop categorical columns and encoded column
df_final.drop(['Director','Title','MPAA Rating','Rating'],axis=1,inplace=True)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_final, label, test_size=0.2, random_state=42)


from sklearn import preprocessing
normalized_train = preprocessing.normalize(X_train)
normalized_test = preprocessing.normalize(X_test)



import statsmodels.api as sm
X_sm = X = sm.add_constant(df_final)
model = sm.OLS(y_train,normalized_train)
model.fit().summary()






from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

 
lm = LinearRegression()
lm.fit(normalized_train,y_train)
scores = cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_squared_error', cv= 95)
rmse_scores = np.sqrt(-scores)
rmse = np.mean(rmse_scores)
print(rmse)



alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
 
    scores = cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_squared_error', cv= 95)
    rmse_scores = np.sqrt(-scores)
    rmse = np.mean(rmse_scores)
    error.append(rmse)
    
plt.plot(alpha,error) 

from sklearn.ensemble import RandomForestRegressor
for i in range(40,75,35):
    print(i)
    regr = RandomForestRegressor(n_estimators=45, random_state=100)
    regr.fit(normalized_train, y_train)
    scores = cross_val_score(regr, normalized_train, y_train,scoring="neg_mean_squared_error", cv=95)
    tree_rmse_scores = np.sqrt(-scores)
    rmse = np.mean(tree_rmse_scores)
    print(rmse)


from sklearn.model_selection import GridSearchCV

parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

grid_search = GridSearchCV(regr,parameters,scoring='neg_mean_absolute_error',cv=12)
grid_search.fit(X_train,y_train)
grid_search.best_score_
grid_search.best_estimator_

# forest regression is the best model



import pickle
pickl = {'model': grid_search.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )

file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

model.predict(np.array(list(normalized_test[0])).reshape(1,-1))[0]
list(normalized_test[0])
 