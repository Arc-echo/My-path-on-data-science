# Import file and library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
%matplotlib inline

df = pd.read_csv("Advertising.csv")

# EDA
df.info()
df.describe()
df.head(5)
sns.scatterplot(x = "TV", y = "sales", data = df)
sns.scatterplot(x = "radio", y = "sales", data = df)
sns.scatterplot(x = "newspaper", y = "sales", data = df)

new_df = df.melt("Unnamed: 0", var_name = "Category", value_name = "sales")
sns.scatterplot(x = "Unnamed: 0", y = "sales", hue = "Category", data = new_df)

# Transform file
df_sales = pd.read_csv('Advertising.csv')
df_sales = df_sales[['TV','radio','newspaper','sales']]

# Cost Function
def cost(X, y, w0, w1, w2, w3):
    N = len(X)
    cost = 0
    for i in range(N):
        yhat = w0 + w1*X.iloc[i,0] + w2*X.iloc[i,1] + w3*X.iloc[i,2]
        err = (y[i] - yhat)**2
        cost += err
    return cost/(2*N)

# Train to update the best cost
def train(X,y,lr=0.1, max_iter=50):
    N = X.shape[0]
    y = np.array(y)
    # Init Weights set 0
    w0 = 1
    w1 = 1
    w2 = 1
    w3 = 1
    #Add History
    w0_hist = []
    w1_hist = []
    w2_hist = []
    w3_hist = []
    cost_hist = []
    #Loop Gradient Descent
    for p_iter in range(max_iter):
        djdw0 = 0
        djdw1 = 0
        djdw2 = 0
        djdw3 = 0
        c = cost(X, y, w0, w1, w2, w3)
        w0_hist.append(w0)
        w1_hist.append(w1)
        w2_hist.append(w2)
        w3_hist.append(w3)
        cost_hist.append(c)
        #Summazion for y-yhat and dj w.t. variable
        for i in range(N):
            yhat = w0 + w1*X.iloc[i,0] + w2*X.iloc[i,1] + w3*X.iloc[i,2]
            djdw0 += -(y[i] - yhat)
            djdw1 += -X.iloc[i,0]*(y[i] - yhat)
            djdw2 += -X.iloc[i,1]*(y[i] - yhat)
            djdw3 += -X.iloc[i,2]*(y[i] - yhat)
        #Update Rule for each iteration
        w0 = w0 -(lr*djdw0/N)
        w1 = w1 -(lr*djdw1/N)
        w2 = w2 -(lr*djdw2/N)
        w3 = w3 -(lr*djdw3/N)
    return cost_hist, w0_hist, w1_hist, w2_hist ,w3_hist
  
  # Standarlization
  from sklearn.preprocessing import StandardScaler
  scaler = StandardScaler()
  scaler.fit(df_sales[["TV", "radio", "newspaper"]])
  X = scaler.transform(df_sales[["TV", "radio", "newspaper"]])
  X = pd.DataFrame(X)
  X.columns = ["TV", "radio", "newspaper"]
