# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 10:03:45 2018

@author: lakshmi
"""

 #Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[10,8,5],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[6,8,2],
    [6,7,3],
    [5,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)