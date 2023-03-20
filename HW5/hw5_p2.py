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


img_g = mpimg.imread('g.jpg')
img_h = mpimg.imread('h.jpg')

img_g = img_g.copy()
img_h = img_h.copy()


# In[3]:


img_g.dtype
img_g = img_g.astype(int)
img_h = img_h.astype(int)
plt.imshow(abs(img_g-img_h))
plt.savefig('i.jpg')

