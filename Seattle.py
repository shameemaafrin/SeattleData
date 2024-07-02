#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sb
from numpy import mean
from numpy import median


# In[5]:



os.getcwd()  

#to read the dataset
treedata_orig = pd.read_csv("Trees.csv")
treedata = pd.read_csv("Trees.csv")


# In[6]:


treedata


# In[22]:


sb.barplot(x = treedata["CONDITION_RATING"], y = treedata["OWNERSHIP"], estimator = mean)


# In[8]:


plt.show()


# In[14]:


sb.barplot(x = treedata["CONDITION_RATING"], y = treedata["OWNERSHIP"], estimator = median)


# In[20]:


plt.title("BOX PLOT FOR THE CONDITION")
plt.boxplot(treedata['CONDITION_RATING'])


# In[ ]:




