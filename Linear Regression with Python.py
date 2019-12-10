#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print('Coefficient of determination:', r_sq)
print('Intercept:', model.intercept_)
print('Slope:', model.coef_)

y_pred = model.predict(x)
print('Predicted response:', y_pred, sep = '\n')


# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
get_ipython().run_line_magic('matplotlib', 'inline')

#Read in CSV:
dataset = pd.read_csv('C:/Users/chughes/Downloads/Weather.csv')

#Visualize min and max temps with scatter plot:
dataset.plot(x = 'MinTemp', y = 'MaxTemp', style = 'o')
plt.title('MinTemp vs MaxTemp')
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')

#Visualize max tmep with distance plot:
plt.figure(figsize=(15, 10))
plt.tight_layout()
seabornInstance.distplot(dataset['MaxTemp'])

#Divide data into attributes and labels:
#Must reshape arrays with (-1, 1) to properly manipulate
X = dataset['MinTemp'].values.reshape(-1, 1)
y = dataset['MaxTemp'].values.reshape(-1, 1)

#Split 80% of the data to the training set while 20% of the data is set to test:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Train the algorithm:
regressor = LinearRegression()
regressor.fit(X_train, y_train) 

#Retrieve the intercept:
print(regressor.intercept_) #10.66185201
#Retrieve the slope:
print(regressor.coef_) #0.92033997
#Data means that for every one unit of change in min temp, the change in max temp is about 0.92%

#Make predictions:
y_pred = regressor.predict(X_test)

#Create dataframe given predicted and actual values:
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

#Visualization of predicted vs. actual values as bar graph:
df1 = df.head(25)
df1.plot(kind = 'bar', figsize = (16, 10))
plt.grid(which = 'major', linestyle = '-', linewidth = '0.5', color = 'black')
plt.show()

#Plot straight line with test data:
plt.scatter(X_test, y_test, color = 'gray')
plt.plot(X_test, y_pred, color = 'red', linewidth = 2)
plt.show()
#Straight line indicates algorithm is correct

#Find values for metrics using our test data:
print('Mean absolute error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean squared error:', metrics.mean_squared_error(y_test, y_pred))
print('Root mean squared error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# In[ ]:




