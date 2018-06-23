# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:13:53 2018

@author: lakshmi
"""

# Program to transpose a matrix using nested loop

X = [[10,9],
    [4 ,8],
    [6 ,5]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)