#!/usr/bin/env python
# coding: utf-8

# # Example of Performing Linear Least Squares Fitting

# First we import numpy and matplotlib

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np


# Now let's generate some random data about a trend line

# In[2]:


np.random.seed(119)

npoints = 50

x = np.linspace(0,10.,npoints)

m = 2.0
b = 1.0
sigma = 2.0

y = m*x + b + np.random.normal(scale = sigma, size = npoints)
y_err = np.full(npoints, sigma)


# In[3]:


f = plt.figure(figsize=(7,7))
plt.errorbar(x,y,sigma,fmt='o')
plt.xlabel('x')
plt.ylabel('y')


# # Method #1, polyfit()

# In[4]:


m_fit, b_fit = np.poly1d(np.polyfit(x,y,1,w=1./y_err))
print(f"The slope is {m_fit}")
print(f"The intercept is {b_fit}")

y_fit = m_fit * x + b_fit


# In[7]:


f = plt.figure(figsize=(7,7))
plt.errorbar(x,y,sigma,fmt='rx', label="data")
plt.plot(x,y_fit,label="fit")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=2, frameon=False)


# In[ ]:




