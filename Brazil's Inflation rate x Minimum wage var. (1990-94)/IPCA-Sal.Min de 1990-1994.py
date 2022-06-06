#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bcb import sgs
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sidetable as sbn


# In[8]:


plt.style.use('seaborn')


# In[20]:


ipca = sgs.get({'ipca':433}, start = '1990-02-01', end = '1994-07-01')
ipca3=ipca.pct_change().mul(100).ipca.dropna(inplace=True)


# In[10]:


smin = sgs.get ({'salario minimo':1619}, start = '1990-02-01', end = '1994-07-01')


# In[11]:


smin.head(10)


# In[21]:





# In[22]:


smin2 = smin.pct_change ().mul(100)


# In[23]:


plt.plot(ipca)
plt.plot (smin2)
plt.ylabel('variação mensal (%)')
plt.title ('Variação mensal da taxa de inflação e do salário mínimo - Brasil')
plt.gca ().legend(('IPCA','Salário Mínimo'))


# In[ ]:





# In[14]:


from sklearn.linear_model import LinearRegression


# In[15]:


model = LinearRegression().fit(smin, ipca)


# In[16]:


r_sq = model.score (smin, ipca)
print(f"coefficient of determination: {r_sq}")


# In[61]:


print(f"intercept: {model.intercept_}")
print(f"intercept: {model.intercept_}")
print(f"coefficients: {model.coef_}")


# In[17]:


from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

lr= LinearRegression()

X=smin
y=ipca
X = sm.add_constant(X)

model = sm.OLS(y,X)
fitted_model = model.fit()
fitted_model.summary()

