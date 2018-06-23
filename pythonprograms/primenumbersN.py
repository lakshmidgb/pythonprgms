# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:32:02 2018

@author: lakshmi
"""

N = int(input("Enter upper range: "))

print("Prime numbers upto a given N:")

for num in range(2,N + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)