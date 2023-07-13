#! /usr/bin/env python
# Linear Modelling Notebook
# Fred Meckler, BSGP 7030
# Importing the dataset

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import sys

print(sys.argv)
if len(sys.argv) <2:
    print ("Missing File Name")
    sys.exist(-1)

print("Running Python linear modelling script")
print()

filename = (sys.argv[1])
print("Loading filename {}" .format(filename))

dataset = pd.read_csv("regrex1.csv")


# Fitting Linear Regression to the Dataset
model = LinearRegression()
model.fit(dataset[['x']], dataset[['y']])

plt.scatter(dataset[['x']], dataset[['y']], color = 'red')
plt.title("X vs Y for {}" .format(filename))
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("{}.png" .format(filename))

LinearRegression
LinearRegression()

# Visualizing the Linear Regression results
plt.scatter(dataset[['x']], dataset[['y']], color = 'red')
plt.plot(dataset[['x']], model.predict(dataset[['x']]), color = 'blue')
plt.title("Model For X vs Y for {}" .format(filename))
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("Model_For_{}.png" .format(filename))

#Adjusted R-squared
model.score(dataset[['x']], dataset[['y']])
