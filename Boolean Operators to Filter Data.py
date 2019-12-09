#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

#Import data file, skip first 4 rows
data = pd.read_csv('C:/Users/chughes/Downloads/medallists.csv', skiprows = 4)
data


# In[2]:


data.Medal == 'Silver'


# In[3]:


#Select dataframe based on who won a silver medal
data[data.Medal == 'Silver']


# In[4]:


#Multiple conditions to filter data
data[(data.Medal == 'Silver') & (data.Gender == 'Men')]


# In[ ]:




