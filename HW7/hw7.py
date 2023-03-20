#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Celia
"""

#%%
"""
# This is an n × n knights tour puzzle game.

"""

import tkinter as Tk


class knights():
   def __init__(self, master, canvas):
       self.master = master
       self.canvas = canvas
       self.past = None
       self.x0 = 0
       self.y0 = 0
       self.count = 0
       self.canvas.bind("<Button-1>", self.rectangle)
       
   def rectangle(self,ev):
       x = ev.x//(w/n)*(w/n)
       y = ev.y//(h/n)*(h/n)
       
       if self.count==0:
           self.past = self.canvas.create_rectangle(x, y, x+(w/n), y+(w/n), fill="orange")
           self.x0 = x
           self.y0 = y
           self.count += 1
           
       elif (abs(x-self.x0)==2*(w/n) and abs(y-self.y0)==1*(w/n)) or (abs(x-self.x0)==1*(w/n) and abs(y-self.y0)==2*(w/n)):
           self.update()
           self.past = self.canvas.create_rectangle(x, y, x+(w/n), y+(w/n), fill="orange")
           self.x0 = x
           self.y0 = y
           self.count += 1
           
       else: 
           print('This move is not valid. Please re-click.')
           
   def update(self):
       self.canvas.itemconfig(self.past, fill='blue')
       

def knights_tour(n):
    for i in range(n+1):
        canvas.create_line(0, h/n*i, w, h/n*i)  #horizontal lines
        canvas.create_line(w/n*i, 0, w/n*i, h)  #vertical lines


if __name__ == "__main__":
    w = 500
    h = 500
    n = 5
    root = Tk.Tk()
    canvas = Tk.Canvas(root, width=w, height=h)
    knights_tour(n)
    canvas.pack()
    
    knights(root, canvas)
    
    root.mainloop()