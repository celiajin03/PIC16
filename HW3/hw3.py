#!/usr/bin/env python
# coding: utf-8

"""
HW3
@author: chenjin

"""
#%%

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return repr(self.data)
    
    
#n  =  Node(10)
#print(str(n))
#print(repr(n))
#print(n)


#%%


class LinkedList:
    def __init__(self,data):
        node = Node(data)
        self.first = node
        self.last = node
        self.n = 1
    def append(self,data):
        new_node = Node(data)
        self.last.next = new_node
        self.last = new_node
        self.n += 1
        
  
    def __iter__(self):
#         self.curr = self.first
#         return self
        return self.generator()
    
#     def __next__(self):
#         if self.curr == None:
#             raise StopIteration
#         data = self.curr.data
#         self.curr = self.curr.next
#         return data
    
    def generator(self):
        curr = self.first
        while (curr):
            data = curr.data
            curr = curr.next
            yield data
    
    def __len__(self):
        return self.n
    
    def __str__(self):
        curr = self.first
        s = '['
        while (curr):
            data = curr.data
            curr = curr.next
            s = s+str(data)+'->'
        s += ']'
        return str(s)
    
    def __repr__(self):
        curr = self.first
        s = '['
        while (curr):
            data = curr.data
            curr = curr.next
            s = s+str(data)+'->'
        s += ']'
        return repr(s)
        
    def __getitem__(self, key):
        if (key > self.n-1 or key < 0):
            raise IndexError('list index out of range')    
        curr = self.first
        for i in range(key):
            curr = curr.next
        return curr.data  
        
    def __setitem__(self, key, value):
        if (key > self.n-1 or key < 0):
            raise IndexError('list index out of range')    
        curr = self.first
        for i in range(key):
            curr = curr.next
        curr.data = value
            
    def __add__(self, other):
        curr = self.first
        copy = LinkedList(curr.data)
        for i in range(self.n-1):
            curr=curr.next
            copy.append(curr)
            
        copy.append(other)
        return copy
        
        
#%%

"""

test code



a = LinkedList(0)
a.append(1)
a.append(2)

print("7 points if this works")
for n in a:
    print(n)

print("")

print("2 points if this works")
for n in a:
    print(n)

print("")

print("3 points if both of these work")
for n in a:
    if n == 2:
        break
    else:
        print(n)

print("")
   
for n in a:
    if n == 2:
        break
    else:
        print(n)

print("")

a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.append(8)

print("")

print("1 points if this works")
print(len(a))
print("")

print("1 points if this works")
print(str(a))
print("")

print("1 points if this works")
print(repr(a))
print("")


print("1 points each. That is, 2 points if the output of the next line is correct")
a[5] = 20
print(a[5])

print("")

print("2 points for correct operation of +")
a+9 # doesn't modify a
print(a)

print("")

a = a+9 # appends 9 to a
print(a)


print("")

print("1 points for raising correct IndexError")
try:
    print(a[999])
except IndexError as e:
    print(e)

print("")


"""