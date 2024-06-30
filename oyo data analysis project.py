#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_excel("D:\\oyo.xlsx")
df.head()


# # Data Understanding

# In[3]:


df.info()


# # Data Preprocessing

# In[4]:


# no data preprocessing is required for this data set -because it is a cleaned data set.


# In[5]:


df.duplicated().sum()


# In[6]:


df.isnull().sum()


# In[7]:


# Top 10 records based on Rating.


# In[8]:


top_10_records = df.nlargest(10, 'Rating')
top_10_records


# In[9]:


# Top 10 records based on Price.


# In[10]:


top_10_records = df.nlargest(10, 'Price')
top_10_records


# In[11]:


# least 10 records based on rating.


# In[12]:


least_10_records=df.nsmallest(10,"Rating")
least_10_records


# In[13]:


# least 10 records based on price.


# In[14]:


least_10_records=df.nsmallest(10,"Price")
least_10_records


# In[15]:


df["Discount"].unique()


# In[16]:


# converting discount of string to integer format.


# In[17]:


df["Discount"]=df["Discount"].str.replace("% off",'').astype(int)


# In[18]:


df["Discount"].unique()


# In[19]:


# describe is used to generate the descriptive statistics of the data in a DataFrame.


# In[20]:


df.describe()


# In[21]:


# splitting the data (location and (price,rating)) into groups based on criteria.


# In[22]:


location_states=df.groupby(["Location"]).agg({"Price":"mean","Rating":"mean"}).reset_index()
print(location_states)


# # Data Visualization

# In[23]:


# based on groupby data visualizing the average prize by location (by using barplot).


# In[24]:


plt.figure(figsize=(100,80))
sns.barplot(x="Location",y="Price",data=location_states)
plt.title("Average price by location")
plt.xticks(rotation=90)
plt.show()


# In[25]:


# visualizing the data how Price and Rating are correlated (by using scatterplot).


# In[26]:


plt.figure(figsize=(10,5))
sns.scatterplot(x="Price",y="Rating",data=df)
plt.title("Price vs Rating")
plt.show()


# In[27]:


# visualizing the data of count of customers based on discount (by using histogram).


# In[28]:


plt.figure(figsize=(10,5))
sns.histplot(df["Discount"])
plt.title("Discount Histogram")
plt.show()


# In[ ]:




