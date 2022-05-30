#!/usr/bin/env python
# coding: utf-8

# In[1]:


import basedosdados as bd

# Para carregar o dado direto no pandas
import pandas as pd
df = bd.read_table(dataset_id='br_ibge_ipca15',
table_id='mes_brasil',
billing_project_id="bustling-walker-349821")


# In[3]:


print (df)


# In[4]:


df.rename(columns={'mes':'mês', 'indice':'índice', 'variacao_mensal':'variação mensal'}, inplace = True)


# In[6]:


df.head(10)


# In[8]:


df.loc[:, 'ano':'índice']


# In[9]:


inf2=df.loc[:,['ano', 'mês', 'índice', 'variação mensal', 'variacao_doze_meses']]


# In[10]:


print (inf2)


# In[11]:


inf01a08=inf2.loc[8:100]


# In[ ]:





# In[12]:


df.loc[1:40]


# In[13]:


inf01a08.head()


# In[14]:


inf01a08.describe()


# In[15]:


a = inf01a08['ano']
i = inf01a08['índice']
j = inf01a08['variacao_doze_meses']
v = inf01a08['variação mensal']
y = [2001, 2002, 2003, 2004]


# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-darkgrid')


# In[115]:


plt.figure (figsize=(8,4))
plt.bar (a, j, color='brown')
plt.ylabel ('variação (%)')
plt.xlabel('ano')
plt.title ('Variação anual do IPCA (%) do Brasil')
plt.style.library['seaborn-darkgrid']
plt.axis ([2000, 2009, 1, 18])

plt.show()


# In[120]:


plt.figure (figsize=(10,5))
plt.plot (a,j, color='grey')


# In[61]:


plt.plot(j,j**2)


# In[20]:


yy=[int(i) for i in y]
print (yy)


# In[21]:


import matplotlib.pyplot as plt
import numpy as np


# In[22]:


hist(v)


# In[23]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('pinfo', 'plt.plot')


# In[24]:


import pandas as pd
import seaborn as sns


# In[113]:


sns.relplot(x='variacao_anual', y='variacao_doze_meses', data=df, hue='variacao_anual')


# In[114]:


plt.plot(j)


# In[78]:


plt.style.available


# In[112]:


plt.style.use('seaborn-darkgrid')


# In[ ]:





# In[ ]:





# In[ ]:





# In[121]:


get_ipython().system('pip install python-bcb')


# In[122]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[123]:


from bcb import sgs
selic = sgs.get({'selic':432}, start = '2010-01-01')


# In[ ]:




