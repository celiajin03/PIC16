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


img_a = mpimg.imread('a.jpg')
centerx = int(img_a.shape[0]/2)
centery = int(img_a.shape[1]/2)
img_a = img_a.copy()


# In[3]:


img_b = mpimg.imread('b.jpg')
xb = int(img_b.shape[0]/2)
yb = int(img_b.shape[1]/2)


# In[4]:


img_a[centerx - xb : centerx + xb, centery - yb : centery + yb] = img_b
plt.imshow(img_a)
plt.savefig('c.jpg')

