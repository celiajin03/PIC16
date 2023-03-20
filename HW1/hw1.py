#!/usr/bin/env python
# coding: utf-8

"""
@author: Chen Jin
"""

#%%
# Problem 1

# function largerIndex(c) takes as input a list c of numbers, and returns a new list k, such that k[i] = 1 if c[i] > i, k[i] = 0 if c[i] = i, k[i] = -1 if c[i] < i.



def largerIndex(c):
    k=[]
    for i in range(len(c)):
        if c[i] > i: k.append(1)
        elif c[i] == i: k.append(0)
        elif c[i] < i: k.append(-1)
    return k



l1 = [1,2,0,4,2,1,40,-5]
l2 = [0,3,2,1,32,3,4,0]
print(largerIndex(l1))
print(largerIndex(l2))



#%%
# Problem 2

# function squareUpTo(n) takes as input a positive integer n, and returns a list of all the square numbers up to (and possibly including) n.


from math import sqrt

def squareUpTo(n):
    square=[]
    for i in range(int(sqrt(n))+1):
         square.append(i**2)
    return square


print(squareUpTo(10))
print(squareUpTo(100))



#%%
# Problem 3

# function flip1in3() uses only “fair coins” to generate a “biased coin” with success probability 1/3


import random as rand

def fliplin3():
    flip = []
    flip = [rand.randint(0, 1), rand.randint(0, 1)]
    if flip == [0,0]: return True
    elif (flip == [0,1]) | (flip == [1,0]): return False
    
    while flip == [1,1]:
        flip = [rand.randint(0, 1), rand.randint(0, 1)]
        if flip == [0,0]: return True
        elif (flip == [0,1]) | (flip == [1,0]): return False


result=[]
for i in range(100000):
    result.append(fliplin3())
result.count(True)/len(result)




#%%
# Problem 4

# function duplicates(c) takes as input a list c of integers and outputs all the elements as a list that appear twice in the list c


def duplicates(c):
    duplicate=[]
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            if c[j]==c[i]:duplicate.append(c[i])
    return duplicate


l3 = [1,2,5,3,6,2,4,5]
l4 = [1,3,5,5,1,4,3]
duplicates(l3)  
duplicates(l4)

