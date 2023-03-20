#!/usr/bin/env python
# coding: utf-8

"""
@author: Chen Jin

"""

import re


#%%
# Problem 1:
def mytype(v):
    v = str(v)
    if '[' in v:
        return 'list'
    elif re.search(r'-?\d+[.]\d+', v) is not None:
        return 'float'
    elif re.match(r'-?\d+', v) is not None:
        return 'int'
    else:
        return 'string'
    


# =============================================================================
# print(mytype(10))
# print(mytype(-10))
# print(mytype(-1.25))
# print(mytype(10.0))
# print(mytype([1, 2, 3]))
# print(mytype([]))
# print(mytype("abc"))
# print(mytype({1,2}))
# =============================================================================





#%%
# Problem 2:

def findpdfs(L):
    return re.findall(r'(\w+)[.]pdf', str(L))



# =============================================================================
# L = ["IMG2309.jpg", "lecture1.pdf", "homework.py", "homework2.pdf"] 
# print(findpdfs(L))
# =============================================================================





#%%
# Problem 3:
import urllib

def findemail(url):
    page = urllib.request.urlopen(url).read().decode()
    p = re.sub(r' AT | at |\[AT\]|\[at\]','@', str(page))
    p = re.sub(r' DOT | dot |\[DOT\]|\[dot\]','.', p)
    return list(set(re.findall(r'(\w+@\w+[.]\w+(?:[.]\w+)?)', p)))



# =============================================================================
# url1 = "https://www.math.ucla.edu/~hangjie/contact/"
# url2 = "https://www.math.ucla.edu/~hangjie/teaching/Winter2019PIC16/regexTest"
# 
# print(findemail(url1))
# print(findemail(url2))
# =============================================================================



#%%
# Problem 4:

from happiness_dictionary import happiness_dictionary as hp
import numpy as np

def happiness(text):
    score = []
    words = set(re.findall(r'\w+', text))
    for word in words:
        try:
            score.append(hp[word.lower()])
        except:
            pass
    return np.mean(score)
    


# =============================================================================
# s1 = "Mary had a little lamb."
# s2 = "Mary had a little lamb. Mary had a little lamb!" 
# s3 = "A quick brown fox jumps over a lazy dog."
# 
# print(happiness(s1))
# print(happiness(s2))
# print(happiness(s3))
# =============================================================================

