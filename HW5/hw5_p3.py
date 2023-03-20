#!/usr/bin/env python
# coding: utf-8
"""
@author: chenjin
"""
# In[1]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all" 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


img_e = mpimg.imread('e.jpg')
img_e = img_e.copy()
plt.imshow(img_e)


# In[3]:


img_d = mpimg.imread('d.jpg')
img_d = img_d.copy()
plt.imshow(img_d)


# In[4]:


x = [i for i in range(img_e.shape[0]) for j in range(img_e.shape[1]) if (img_e[i,j,1] >= 200) & (img_e[i,j,0] <= 100)]
y = [j for i in range(img_e.shape[0]) for j in range(img_e.shape[1]) if (img_e[i,j,1] >= 200) & (img_e[i,j,0] <= 100)]


# In[5]:


img_e[x,y] = [0,0,0]
plt.imshow(img_e)


# In[6]:


img_e.shape
img_d.shape


# In[7]:


for i in range(img_e.shape[0]):
    for j in range(img_e.shape[1]):
        if all(img_e[i,j] != [0,0,0]):
            img_d[580+i, 255+j] = img_e[i,j]
plt.imshow(img_d)
plt.savefig('f.jpg')




