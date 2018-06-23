# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:11:08 2018

@author: lakshmi
"""

def fact(n):
    if n>0:
        return n*fact(n-1)
    return 1
m = fact(10)
print(m)

def details(name, age=40): 
    print("Name", name )
    print ("age", age )
details("Rohit", age=28) 
details("Ravi") 

def f(a,b,x,y):
    print(a,b,x,y)
d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
print(f(**d))

#while loop example
n = 10
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

#Nested loop example
for i in range (1, 3, 1):
    for j in range (1, 4, 1):
        print( "i = ", i, " j = ", j)
print( "Done!")

#function returning multiple values

def square(x,y):
 return [ x*x, y*y ]

L1 = square(2,3)
print(L1)

