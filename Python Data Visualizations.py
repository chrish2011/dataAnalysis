#!/usr/bin/env python
# coding: utf-8

# In[1]:


import timeit

def reverse_join(s):
    return "".join(reversed(s))
def slice_notation(s):
    return s[::-1]
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
reverse_join_times = timeit.repeat(lambda: reverse_join(s))
slice_notation_times = timeit.repeat(lambda: slice_notation(s))
avg_reverse = sum(reverse_join_times)/len(reverse_join(s))
avg_slice = sum(slice_notation_times)/len(slice_notation_times)
print(avg_reverse)
print(avg_slice)
print(avg_reverse / avg_slice)


# In[8]:


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#create list of months
Month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 
         'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#create list for made up average temperatures
Avg_Temp = [35, 45, 55, 65, 75, 85, 95, 100, 85, 65, 45, 35]
#create list for made up average percipitation %
Avg_Percipitation_Perc = [.90, .75, .55, .10, .35, .05, .05, .08, .20, .45, .65, .80]

#Assign lists to value
data = {'Month': Month, 'Avg_Temp': Avg_Temp, 'Avg_Percipitation_Perc': Avg_Percipitation_Perc}

#Convert dicitonary to dataframe
#df = pd.DataFrame(data)
#df[:12]

#Create bar chart for average temps by month
#plt.title('Average Temperature by Month')
#sns.barplot(x = 'Month', y = 'Avg_Temp', data = df, palette = 'summer')

#Create line plot for average percipitation levels
#plt.title('Average Percipitatoin Percentage by Month')
#sns.lineplot(x = 'Month', y = 'Avg_Percipitation_Perc', data = df, sort = False)

#Create combo chart
fig, ax1 = plt.subplots(figsize=(10,6))
color = 'tab:green'
ax1.set_title('Average Percipitation Percentage by Month', fontsize=16)
ax1.set_xlabel('Month', fontsize=16)
ax1.set_ylabel('Avg Temp', fontsize=16, color=color)
ax2 = sns.barplot(x='Month', y='Avg_Temp', data = df, palette='summer')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Avg Percipitation %', fontsize=16, color=color)
ax2 = sns.lineplot(x='Month', y='Avg_Percipitation_Perc', data = df, sort=False, color=color)
ax2.tick_params(axis='y', color=color)
plt.show()


# In[24]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline #use it to show plot directly below the code

df = pd.read_csv('C:/Users/chughes/Downloads/2019.csv')
#df.head()

#sns.distplot(df['GDP per capita'], bins = 8)
#out[5]
#sns.distplot(df['GDP per capita'], kde = False, bins = 30)
#out[6]

#Joint plot
#sns.jointplot(x = df['GDP per capita'], y = df['Healthy life expectancy'], data = df)

#sns.jointplot(x = df['GDP per capita'], y = df['Healthy life expectancy'], data = df, kind = 'reg')
#sns.jointplot(x = df['GDP per capita'], y = df['Healthy life expectancy'], data = df, kind = 'hex')
#sns.pairplot(df) #relationship entire datasets

sns.barplot(x = df['Country or region'].head(3), y = df['GDP per capita'], data = df)


# In[27]:


data_select = df[['GDP per capita', 'Social support', 'Healthy life expectancy', 'Perceptions of corruption']]
data_select.corr()
sns.heatmap(data_select.corr(), cmap = 'coolwarm')


# In[28]:


data = df[['Healthy life expectancy', 'GDP per capita']]
layout = dict(title = 'Line Chart from Pandas Dataframe', xaxis = dict(title = 'x-axis'), yaxis = dict(title = 'y-axis'))
data.iplot(filename = 'cf-simple-line-chart', layout = layout)


# In[29]:




data1=go.Scatter(x=df['Country or region'],y=df['GDP per capita'], name="GDP per capita", mode="markers") 
data2=go.Scatter(x=df['Country or region'],y=df['Healthy life expectancy'],name="Healthy life expectancy",mode="markers")
mydata = go.Data([data1, data2])
mylayout = go.Layout( title="GDP per capita vs. Life expectancy")
fig = go.Figure(data=mydata, layout=mylayout)
chart_studio.plotly.iplot(fig)


# In[31]:


#Boolean indexing:
import pandas as pd
df = pd.DataFrame({'EmployeeName': ['John', 'Sam', 'Sara', 'Nick', 'Bob', 'Julie'],
                 'Salary': [5000, 8000, 7000, 10000, 3000, 5000]})

salary_bool = df['Salary'] == 5000
salary_5000 = df[salary_bool]
print(salary_5000)


# In[ ]:




