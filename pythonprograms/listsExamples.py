# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:16:53 2018

@author: lakshmi
"""

lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst)
#Replace [30,40,50] segment with values in list[á','b','c']
lst[2:5] = ['a','b','c']
print(lst)
lst = [10, 20, 30, 40, 50, 60, 70, 80]
#Replace at index 2  with values in list[á','b','c']
lst[2:2] = ['a','b','c']
print(lst)