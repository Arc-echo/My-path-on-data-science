# Import files
import pandas as pd
import numpy as np
df_test = pd.read_csv("test.csv")
df_train = pd.read_csv("train.csv")

#Prepare dataset for prediction  
# Sex, age, Pclass, sibsp, parch, fare, Cabin[First letter], Survived
# Fill missing age, Cabin
# Use get_dummies on Cabin, Sex
# Optional: bin age

def feature_enginnering_func(df, age_mean, fare_mean):
    df["Age"] = df["Age"].fillna(age_mean)
    df["Age_Group"] = df["Age"]//10 #qcut

    #Cabin
    df["Cabin_code"] = df["Cabin"].str[0]
    df["Cabin_code"] = df["Cabin_code"].fillna("Z")
    
    #Fare
    df["Fare"] = df["Fare"].fillna(fare_mean)

    #get_dummy
    df = pd.get_dummies(df, columns=["Sex", "Cabin_code", "Age_Group"]).drop(columns=["Cabin","Age"])
    
    return df
  
#for i in list(set(list(df_train_s["Cabin_code"]))):
#    df_train_s["Cabin_{}".format(i)] = df_train_s["Cabin_code"].apply(lambda x: 1 if x == i else 0)

#Last step: Put our dataset for prediction
df_train_s = df_train[["Sex","Age","Pclass","SibSp","Parch","Fare","Cabin","Survived"]]
age_mean = df_train_s["Age"].mean()
fare_mean = df_train_s["Fare"].mean()
df_train_s = feature_enginnering_func(df_train_s, age_mean,fare_mean)

df_test_s =  df_test[["Sex","Age","Pclass","SibSp","Parch","Fare","Cabin"]]
df_test_s = feature_enginnering_func(df_test_s, age_mean,fare_mean)

# Prepare X_train and y_train
X_train = df_train_s.drop(columns=["Survived"])
y_train = df_train_s["Survived"]

# Set dummies to 0
X_test = df_test_s
X_test["Age_Group_8.0"] = 0
X_test["Cabin_code_T"] = 0

from sklearn.linear_model import LogisticRegression

logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)  #Build Algo

y_train_predict = logistic_model.predict(X_train)
y_test_predict = logistic_model.predict(X_test)

#Extract the result to csv file
df = pd.DataFrame(data = y_test_predict, index = indexes, columns = ["Survived"])
df["PassengerId"] = df.index
new_df = df[["PassengerId", "Survived"]]
new_df = new_df.reset_index(drop = True)
new_df.to_csv("submission.csv")
new_df = new_df.set_index("PassengerId")
