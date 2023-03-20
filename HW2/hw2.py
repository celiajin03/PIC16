#!/usr/bin/env python
# coding: utf-8
"""
@author: chenjin

"""

#%%
"""
Problem 1

the function longestpath() finds the length of the longest path in a dictionary d without considering circles

"""


def longestpath(d):
    loop = []
    for key in list(d):
        path = []
        length = 0
        path.append(key)

        try:
            key = d[key]

            while (key not in path):
                path.append(key)
                length+=1
                try:
                    key = d[key]
                except:
                    length-=1
        except:
            break
        loop.append(length)
    return max(loop)+1




# d1 = {"a":"b","b":"c"}
# d2 = {"a":"b","b":"c","c":"d","e":"a","f":"a","d":"b"}

# print(longestpath(d1))
# print(longestpath(d2))



#%%
"""
Problem 2

This function implements the Newton-Raphson method.
The solve function takes as input a function f(x), its derivative f′(x), an initial guess x0 and the tolerance ε.
It finds a desired value x∗ which is close enough to a root of f(x) such that |f(x∗)| ≤ ε.

"""


import math

def solve(f,x0,ε):
    while abs(f(x0)[0])>ε:
        x1=x0-f(x0)[0]/f(x0)[1]
        x0=x1
    return x0



# print(solve(lambda x: [x**2-1, 2*x], 3, 0.0001))
# print(solve(lambda x: [x**2-1, 2*x], -1, 0.0001))
# print(solve(lambda x: [math.exp(x) - 1, math.exp(x)], 1, 0.0001))
# print(solve(lambda x: [math.sin(x), math.cos(x)], 0.5, 0.0001))





