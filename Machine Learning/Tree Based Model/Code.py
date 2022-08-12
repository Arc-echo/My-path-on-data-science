# Import libaries
from itertools import product, combinations, permutations
import random
import math

from sklearn import datasets
import numpy as np
import pandas as pd
from scipy import stats

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report

import xgboost as xgb

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## load data
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

# Prepare data sets
X = df_train.drop(columns = ["label"]).to_numpy()
y = df_train["label"]
X_test = df_test.to_numpy()

# Standalization
X_nor = X/255
X_train, X_test, y_train, y_test = train_test_split(X_nor, y, test_size = 0.3, random_state = 99)

# Transfrom to D Matrix
dtrain = xgb.DMatrix(X_train, label=y_train)
dval = xgb.DMatrix(X_test, label = y_test)
dtest = xgb.DMatrix(df_test.values/255)

param = {'max_depth':2, 'eta':1, 'objective':'multi:softmax', 'num_class': 10 }
num_round = 2
bst_train = xgb.train(param, dtrain, num_round)
bst_val = xgb.train(param, dval, num_round)
# make prediction
preds_train = bst_train.predict(dtest)
preds_val = bst_val.predict(dtest)

from sklearn.model_selection import ParameterGrid
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
param_dict = {
    "max_depth" : [6,8],
    "eta" : [0.3, 0.5],
    'objective': ['multi:softmax'],
    'num_class': [10],
    'gamma' : [0.2,0.3]
    }

# Based on the combination of parameters -> search for the best parameter for the model
best_score = 0
for param in ParameterGrid(param_dict):
    num_round = 5
    #Training
    bst = xgb.train(param, dtrain, num_round)
    #Prediction
    ypred_train = bst.predict(dtrain)
    ypred_val = bst.predict(dval)
    #Evaluation
    train_score = accuracy_score(y_train, ypred_train)
    val_score = accuracy_score(y_test, ypred_val)
    print("Accuracy Score: Train:{}, Val:{}".format(train_score, val_score))
    if val_score > best_score:
        best_score = val_score
        best_param = param
        print("Best Score and best para", best_score, best_param)
        
# By using GridSearch -> search for the best parameter for the model
from sklearn.model_selection import GridSearchCV
param_grid = {"max_depth" : [6,8],
    "eta" : [0.3, 0.5],
    'objective': ['multi:softmax'],
    'num_class': [10],
    'gamma' : [0.2,0.3]}
model = GridSearchCV(xgb.XGBClassifier(), param_grid, n_jobs = 5)
model.fit(X_train, y_train)

print("Best kernel: ", model.best_params_)
