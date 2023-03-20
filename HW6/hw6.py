#!/usr/bin/env python
# coding: utf-8
"""
@author: chenjin
"""
# In[1]:

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all" 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#%%
"""
Problem 1:
The function heart(im) takes an image im as input, and outputs a heart-shaped cut-out of it on a pink background. The shape of the heart depend on the dimensions of the image.
"""

# =============================================================================
# img = mpimg.imread('cat.jpg')
# img = img.copy()
# plt.imshow(img)
# =============================================================================



def heart(im):
    y1= lambda x : -np.sqrt(1-(abs(x)-1)**2)+1
    y2= lambda x : 3*np.sqrt(1-(abs(x)/2)**0.5)+1
    
    for j in range(im.shape[1]):
        for i in range(im.shape[0]):
            y = i/im.shape[0]*4 
            x = j/im.shape[1]*4-2    
            if not (y>y1(x)) & (y<y2(x)):
                im[i,j] = [255,192,203]
    return im


# =============================================================================
# plt.imshow(heart(img))
# plt.show()
# =============================================================================


#%%
"""
Problem 2:
The function blurring(im, method) takes a gray-scale picture, and offers two options for noise blurring: uniform or Gaussian.
"""

# =============================================================================
# img = mpimg.imread('greyImg.png')
# img = img.copy()[:,:,0:3]
# plt.imshow(img)
# =============================================================================



def blurring(im, method):
    img=im.copy()
    k=5
    a=int((k-1)/2)
    
    if method == 'uniform':
        filter = np.array([[1.0/k**2]*k]*k)
        
    elif method == 'Gaussian':
        sigma = 1
        filter = np.array([[0]*k]*k, dtype='float')
        for x in range(k):
            for y in range(k):
                filter[x,y]=np.exp(-((x-(k-1)*0.5)**2+(y-(k-1)*0.5)**2)/(2.0*sigma**2))
        filter_sum = np.sum(filter)
        filter = filter/filter_sum
        
        
    for i in range(a,im.shape[0]-a):
        for j in range(a,im.shape[1]-a):
            img[i,j] = np.sum(filter*im[(i-a):(i+a+1),(j-a):(j+a+1),0])
    return img




# =============================================================================
# plt.imshow(blurring(img, 'uniform'))
# plt.show()
# plt.imshow(blurring(img, 'Gaussian'))
# plt.show()
# =============================================================================



#%%
"""
Problem 3:
The function detect_edge(im, method) takes a gray-scale image and detects edges, with the option of horizontal, vertical or both.
"""

# =============================================================================
# img = mpimg.imread('rectangle.jpg')
# img = img.copy()/255.0
# plt.imshow(img)
# =============================================================================




def detect_edge(im, method):
    k=3
    a=int((k-1)/2)
    img=im.copy()
    vertical_filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    horizontal_filter = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    
    
    for i in range(a,im.shape[0]-a):
        for j in range(a,im.shape[1]-a):
            S_H = np.sum(horizontal_filter*im[(i-a):(i+a+1),(j-a):(j+a+1),0])
            S_V = np.sum(vertical_filter*im[(i-a):(i+a+1),(j-a):(j+a+1),0])
            
            if method == 'horizontal':
                img[i,j] = (S_H+4)/8
            elif method == 'vertical':
                img[i,j] = (S_V+4)/8
            elif method == 'both':
                img[i,j] = np.sqrt(S_H**2+S_V**2)/(32**0.5)
    return img




# =============================================================================
# plt.imshow(detect_edge(img, 'horizontal'))
# plt.show()
# plt.imshow(detect_edge(img, 'vertical'))
# plt.show()
# plt.imshow(detect_edge(img, 'both'))
# plt.show()
# 
# =============================================================================


