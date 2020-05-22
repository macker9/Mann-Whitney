#!/usr/bin/env python
# coding: utf-8

# In[16]:


#import essential function
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # import data

# In[17]:


#import excel file of PERLE 2 cruise
data = pd.read_excel(r'C:\Users\maria\Dropbox (MIT)\PERLE cruise\33P\33P final values summary.xlsx') #place r before the pathstring
print(data)


# In[18]:


#define variables
D = data['Depth']
Pi = data['Pi concentration']
R = data['N/P']
u = data['% Pi uptake']
T = data['Turnover']
U = data['Pi uptake']
phn = data['% phn']
Phn = data['Phn production']
print(D)
print(Pi)


#  Mann Whitney U function

# In[20]:


from scipy.stats import mannwhitneyu

variables = [D, Pi, R, u, T, U, phn, Phn] #make a list of variables

for i, j in variables:
    statistic, pvalue = mannwhitneyu(i, j, use_continuity=True, alternative='two-sided')



# # Create a Table

# In[ ]:


np.array(names)=variables

