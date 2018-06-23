# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:52:30 2018

@author: lakshmi
"""

# Program to add two matrices using nested loop

X = [[10,8,5],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[6,8,2],
    [6,7,3],
    [5,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)