#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
amazon = pd.read_csv('C:/Users/chughes/Downloads/amazon.csv', encoding = 'ISO-8859-1')

amazon.iloc[3848:3856]['number']
amazon['number'] = amazon['number'].apply(np.round)
amazon['year'].max()


# In[12]:


acre_fires = sum(amazon[amazon['state'] == 'Acre']['number'])
print("Number of fires in Acre state are {}".format(acre_fires))


# In[19]:


#Use boolean indexing to get only 'Acre' state subset and assign to variable 'amazon_acre'
#'amazon_acre' will generatea series which shows True and False for each row based on the condition
amazon_acre = amazon['state'] == 'Acre'
#Use the above series to index the entire dataset and assign it to variable 'amazon_acre_data'
amazon_acre_data = amazon[amazon_acre]
#Variable to store number of fires in each state
amazon_acre_number = amazon_acre_data['number']
#Use sum() function with 'amazon_acre_number' to find total number of fires
amazon_acre_number.sum()
#Use groupby() method on 'year' to get total number of fires for each year
acre_fires_year = amazon[amazon['state'] == 'Acre'].groupby('year').sum()
#Display first five rows
acre_fires_year.head(5)
#Reset_index() method to make index be treated as column
acre_fires_year.reset_index(inplace = True) #inplace = True is used to make permanent changes to underlying data
acre_fires_year.head(5)


# In[25]:


import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure(figsize = (12, 5))
sns.barplot(x = 'year', y = 'number', data = acre_fires_year)


# In[26]:


#Visualize total number of fires by state in all states
#Use groupby() on 'state' column to find total number of fires
total_fires = amazon.groupby('state')['number'].sum().reset_index()
fig = plt.figure(figsize = (25, 10))
sns.barplot(x = 'state', y = 'number', data = total_fires)


# In[27]:


#Find total number of fires in 2017 and visualize data based on each 'month'
total_fires_2017 = amazon[amazon['year'] == 2017][['number', 'month']].groupby('month').sum().reset_index()

fig = plt.figure(figsize = (10, 4))
sns.barplot(x = 'month', y = 'number', data = total_fires_2017)


# In[28]:


#Find average number of fires
avg_fires = amazon['number'].mean()
avg_fires


# In[30]:


#Find out state names where fires occurred in December
dec_fires = amazon[amazon['month'] == 'Dezembro']['state'].unique()
print("Below is a list of states in Brazil where fires occurred in December: \n{}".format(dec_fires))


# In[ ]:




