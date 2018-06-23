# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 19:00:56 2018

@author: lakshmi
"""
#Replaces all v and b in the original sentence with b and v respectively
s=input("Enter a sentence :")
for ch in s:
    if ch =='v':
        s = s.replace('v', 'v1')
    s1 = s.replace('b', 'v')
    s2 = s1.replace('v1','b')
print(s2) 
#print(s.replace('b', 'v'))