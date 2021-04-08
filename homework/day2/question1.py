# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:41:56 2021

@author: ozgur
"""

mylist = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
len = len(mylist)
mid = int(len / 2)

x = mylist[:mid],mylist[mid:] = mylist[mid:],mylist[:mid]

print(x)