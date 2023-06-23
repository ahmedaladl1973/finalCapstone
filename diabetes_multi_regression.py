#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:18:55 2023

@author: ahmedaladl
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

'''
# Load data 
df = pd.read_csv('diabetes2.csv')

# Determine your independent and dependent variables
X = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
         'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']].values
y = df['Outcome'].values # Diabetes outcome: 1 = yes, 0 = no

# Fitting the logistic regression model
clf = LogisticRegression().fit(X, y)

# Coefficients and intercept
print("Coefficients: ", clf.coef_)
print("Intercept: ", clf.intercept_)

# Make a prediction
y_pred = clf.predict([[0, 180, 70, 23, 94, 31, 0.351, 45]])
print("Outcome: ", y_pred)

sns.scatterplot(data=df, x='Glucose', y='Outcome')
plt.show()

'''

# Load the data
df = pd.read_csv('diabetes2.csv')

# Create the X and y variables

print('regnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
         'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age')

feature = input("Chose a feature to polt from above")
X = df[[feature]].values
y = df['Outcome'].values

# Plot the scatter plot
plt.scatter(X, y)

# Label the axes
plt.xlabel(fearure)
plt.ylabel('Outcome')

# Show the plot
plt.show()