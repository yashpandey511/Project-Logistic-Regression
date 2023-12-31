# -*- coding: utf-8 -*-
"""Logistic Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13NsicfvRrBNOP4Jcf8LItev7YIFULoKX

This data given by an airline organization. The actual name of the company is not given due to various purposes that's why the name Invistico airlines.

The dataset consists of the details of customers who have already flown with them. The feedback of the customers on various context and their flight data has been consolidated.

The main purpose of this dataset is to predict whether a future customer would be satisfied with their service given the details of the other parameters values.

Also the airlines need to know on which aspect of the services offered by them have to be emphasized more to generate more satisfied customers.

#Important Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

"""# Read Data"""

df = pd.read_csv('Airline.csv')

df

"""#Explore Data in Depth"""

df.shape

df.columns

df.dtypes

df.count()

df.isnull().sum()

df.head()

df.head(10)

df.tail()

df.tail(10)

df.sample()

df.sample(5)

df[0:10]

df.info()

df.describe()

"""#Replacing Satisfaction with dummy variables"""

sat = pd.get_dummies(df['satisfaction'],drop_first=True)

df= pd.concat([df,sat],axis=1)

gen = pd.get_dummies(df['Gender'],drop_first=True)

df= pd.concat([df,gen],axis=1)

ct = pd.get_dummies(df['Customer Type'],drop_first=True)

df= pd.concat([df,ct],axis=1)

df

df.drop('satisfaction',axis=1,inplace=True)

df.drop('Gender',axis=1,inplace=True)

df.drop('Customer Type',axis=1,inplace=True)

df

df.rename(columns=({ 'satisfied': 'Satisfaction'}), inplace=True)

df.rename(columns=({ 'Male': 'Gender'}), inplace=True)

df.rename(columns=({ 'disloyal Customer': 'Loyal Customer'}), inplace=True)

df

"""#Visualization of Data"""

df.hist(figsize = (20,20))

df.corr()

sn.heatmap(df.corr())

sn.countplot(x='Satisfaction',data=df)
plt.show()

sn.scatterplot(x='Departure Delay in Minutes', y='Arrival Delay in Minutes',data=df)
plt.show()

sn.distplot(df['Flight Distance'])

"""#Data Cleaning"""

df.isnull().sum()

df['Arrival Delay in Minutes'].fillna(df['Departure Delay in Minutes'].mean(), inplace = True)

df

df.isnull().sum()

df.drop('Age',axis=1,inplace=True)

df.drop('Type of Travel',axis=1,inplace=True)

df.drop('Class',axis=1,inplace=True)

df

"""# Decide Dependant and Independant Elements in Data Set"""

x=df.drop('Satisfaction',axis=1)

x

y=df['Satisfaction']

y

"""#Train Test Split"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=0.3)

X_train.info()

X_test.info()

"""#Machine Learning Models

1. Linear
2. Logistic
3. SVC
4. KNN
5. K Mean
6. Desicion Tree
7. Random Forest
8. Naive Bayes

#Logistic Regression
"""

from sklearn.linear_model import LogisticRegression #Importing LogisticRegression Module from sklearn.linear_model library

logmodel = LogisticRegression()

logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report #Importing classification_report Module from sklearn.metrics library

print(classification_report(y_test,predictions))