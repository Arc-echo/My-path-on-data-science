# Import neccessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score, plot_roc_curve
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

# Import Files
file= pd.read_csv("Iris.csv")
# Prepare data sets
X_train_t = file.drop(columns=["Species", "Id"])
X_train_t_Standard = StandardScaler().fit_transform(X_train_t)# Fit is more suitable if test set is available
y_train_t = file["Species"]

# Split Train Sets And Validation Sets
X_train, X_val, y_train, y_val = train_test_split(X_train_t_Standard, y_train_t, test_size = 0.3, random_state = 42)

# Build a logistic model
logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)

y_pred_train_log = logistic_model.predict(X_train)
y_pred_val_log = logistic_model.predict(X_val)

# Build SVM Models

# Linear
clf_linear = SVC(kernel = "linear")
clf_linear.fit(X_train, y_train)

y_pred_train_SVM_linear = clf_linear.predict(X_train)
y_pred_val_SVM_linear = clf_linear.predict(X_val)

# Poly
clf_poly = SVC(kernel = "poly")
clf_poly.fit(X_train, y_train)

y_pred_train_SVM_poly = clf_poly.predict(X_train)
y_pred_val_SVM_poly = clf_poly.predict(X_val)

# RBF
clf_rbf = SVC(kernel = "rbf")
clf_rbf.fit(X_train, y_train)

y_pred_train_SVM_rbf = clf_rbf.predict(X_train)
y_pred_val_SVM_rbf = clf_rbf.predict(X_val)

# Sigmoid
clf_sig = SVC(kernel = "sigmoid")
clf_sig.fit(X_train, y_train)

y_pred_train_SVM_sig = clf_sig.predict(X_train)
y_pred_val_SVM_sig = clf_sig.predict(X_val)

# Compare the accuracies

acc_train_log = accuracy_score(y_train, y_pred_train_log)
acc_val_log = accuracy_score(y_val, y_pred_val_log)
print("Accuracy for Train (Logistic Model): {0}, Accuracy for Val (Logistic Model): {1}". format(acc_train_log, acc_val_log))

acc_train_SVM_linear = accuracy_score(y_train, y_pred_train_SVM_linear)
acc_val_SVM_linear = accuracy_score(y_val, y_pred_val_SVM_linear)
print("Accuracy for Train (SVM_linear): {0}, Accuracy for Val (SVM_linear): {1}". format(acc_train_SVM_linear, acc_val_SVM_linear))

acc_train_SVM_poly = accuracy_score(y_train, y_pred_train_SVM_poly)
acc_val_SVM_poly = accuracy_score(y_val, y_pred_val_SVM_poly)
print("Accuracy for Train (SVM_poly): {0}, Accuracy for Val (SVM_poly): {1}". format(acc_train_SVM_poly, acc_val_SVM_poly))

acc_train_SVM_rbf = accuracy_score(y_train, y_pred_train_SVM_rbf)
acc_val_SVM_rbf = accuracy_score(y_val, y_pred_val_SVM_rbf)
print("Accuracy for Train (SVM_rbf): {0}, Accuracy for Val (SVM_rbf): {1}". format(acc_train_SVM_rbf, acc_val_SVM_rbf))

acc_train_SVM_sig = accuracy_score(y_train, y_pred_train_SVM_sig)
acc_val_SVM_sig = accuracy_score(y_val, y_pred_val_SVM_sig)
print("Accuracy for Train (SVM_sig): {0}, Accuracy for Val (SVM_sig): {1}". format(acc_train_SVM_sig, acc_val_SVM_sig))

#Confusion Matrics - Recall Precision
print(confusion_matrix(y_train, y_pred_train_log))
print(confusion_matrix(y_val, y_pred_val_log))

print(confusion_matrix(y_train, y_pred_train_SVM_linear))
print(confusion_matrix(y_val, y_pred_val_SVM_linear))

print(confusion_matrix(y_train, y_pred_train_SVM_poly))
print(confusion_matrix(y_val, y_pred_val_SVM_poly))

print(confusion_matrix(y_train, y_pred_train_SVM_rbf))
print(confusion_matrix(y_val, y_pred_val_SVM_rbf))

print(confusion_matrix(y_train, y_pred_train_SVM_sig))
print(confusion_matrix(y_val, y_pred_val_SVM_sig))

# Find the best kernel
param_grid = {"kernel" : ["linear", "rbf", "poly", "sigmoid"]}
model = GridSearchCV(SVC(), param_grid)
model.fit(X_train, y_train)

print("Best kernel: ", model.best_params_)
