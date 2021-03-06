# -*- coding: utf-8 -*-
"""recruitment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QxYny0xlM1RXQhg9o8XtIVJ29ARNP5sj

**APPLICATION OF MACHINE LEARNING IN RECRUITMENT**

IMPORTING THE LIBRARIES
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

"""IMPORTING THE DATASET"""

dataset=pd.read_csv("Placement_Data_Full_Class.csv")
dataset

dataset.describe()

"""EXPLORATORY DATA ANALYSIS"""

plt.figure(figsize=(14,25))
for i,j in zip(num,range(1,len(num)+1)):
    plt.subplot(5,2,j)
    sns.boxplot(dataset[i],color='lightblue')
plt.show()

plt.figure(figsize=(10,7))
sns.heatmap(dataset.corr(),annot=True, cmap="Purples")
plt.show()

sns.countplot(dataset['degree_t'])
dataset['degree_t'].value_counts(normalize=True)

dataset.info()

"""ENCODING THE CATEGORICAL VARIABLES"""

from sklearn.preprocessing import LabelEncoder
labels=LabelEncoder()

dataset['gender']=labels.fit_transform(dataset['gender'])
dataset['ssc_b']=labels.fit_transform(dataset['ssc_b'])
dataset['hsc_b']=labels.fit_transform(dataset['hsc_b'])
dataset['hsc_s']=labels.fit_transform(dataset['hsc_s'])
dataset['degree_t']=labels.fit_transform(dataset['degree_t'])
dataset['workex']=labels.fit_transform(dataset['workex'])
dataset['specialisation']=labels.fit_transform(dataset['specialisation'])
dataset['status']=labels.fit_transform(dataset['status'])

dataset

X=dataset.drop(['status'], axis=1)
Y=dataset['status']

"""SPLITTING THE DATASET INTO THE TRAINING SET AND TESTING SET"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.25, random_state=0)
print(X_train)

print(y_train)

"""TRAINING THE MODEL IN THE TRANING SET"""

from sklearn.linear_model import LogisticRegression
logreg= LogisticRegression(solver='liblinear')
logreg

logreg.fit(X_train, y_train)

"""PREDICTING THE MODEL IN THE TESTING SET"""

pred_train=logreg.predict(X_train)
pred_train

pred_test=logreg.predict(X_test)
pred_test

"""MAKING CONFUSION MATRIX"""

from sklearn.metrics import confusion_matrix, accuracy_score,recall_score,roc_auc_score,precision_score,f1_score
print("Test confusion matrix :\n",confusion_matrix(pred_test, y_test))
print("Training Accuracy :",accuracy_score(pred_train, y_train)*100)
print("Test Accuracy :",accuracy_score(pred_test, y_test)*100)
print("Precision :",precision_score(pred_test, y_test)*100)
print("Recall :",accuracy_score(pred_test, y_test)*100)
print("F1-score",f1_score(pred_test, y_test)*100)