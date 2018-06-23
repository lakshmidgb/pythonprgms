# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 20:31:03 2018

@author: lakshmi
"""

arr = [1,2,3,4,5,6,7] 
print(len(arr))

#python array slice 
arr1 = arr[0:3] 		#start(0) to index 2 
print(arr1) 

arr1 = arr[2:] 		#index 2 to end of arr
print(arr1) 

arr1 = arr[:3] 		#start to index 2
print(arr1) 

arr1 = arr[:] 		#copy of whole arr 
print(arr1) 

arr1 = arr[1:6:2] 		# from index 1 to index 5 with step 2 
print(arr1) 

#insertion at specified index
arr = [1,2,3,4,5,6,7] 
arr.insert(3,10) 
print(arr)
#removal of an element at specified index
arr.pop(3)
print(arr)

#array repetition
arr = ['a']
print(arr*5)



