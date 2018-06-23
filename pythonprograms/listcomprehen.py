# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:58:29 2018

@author: lakshmi
"""
evens = [n for n in range(1,21) if n%2 == 0]
print(evens)

#transpose = [[row[n] for row in matrix] for n in range(4)]

a=int(input("enter no.of rows:"))
b=int(input("enter no.of columns:"))
x= [[input("enter the elements of mat1:") for j in range(b)]for i in range(a)]
y= [[input("enter the elements of mat2:") for j in range(b)]for i in range(a)]
result = [[int(x[i][j]) + int(y[i][j]) for j in range(0,b)] for i in range(0,a)]
print(result)
#Matrix2 = [[] for vr in range(0, c)]
#for vr in range(0, c):
#    Matrix2[vr] = [0 for vc in range(0, v)]
#    
#l =[[0 for i in range(0,3)] for j in range(0,4)]
#print(l)

