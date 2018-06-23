# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 10:03:27 2018

@author: lakshmi
"""

name = [ "Manjeet", "Nikhil", "Sharan", "Ayesha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60,70 ]
 
# using zip() to map values
mapped = zip(name, roll_no, marks)
#testList = list(mapped)
for values in mapped :
    print(values)
    
#Extracting the zip
#testList = list(mapped)
#
#a, b,c = zip( *testList )
#print('The first list was ', list(a))
#print('The second list was ', list(b))
#print('The third list was ', list(c))
    
list_a = ['a', 'b', 'c', 'd', 'e']
list_b = [1, 2, 3]

zipped_list = list(zip(list_a, list_b))
print(zipped_list)