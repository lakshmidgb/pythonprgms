# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:38:10 2018

@author: lakshmi
"""

# Python program for implementation of stack
 
Maxsize=10
 
# Function to create a stack. It initializes size of stack as 0
def createStack():
    stack = []
    return stack
 
# Stack is empty when stack size is 0
def isEmpty(stack):
    return len(stack) == 0
 
# Function to add an item to stack. It increases size by 1
def push(stack, item):
    stack.append(item)
    print("pushed to stack " + item)
     
# Function to remove an item from stack. It decreases size by 1
def pop(stack):
    if (isEmpty(stack)):
        return "stack empty no element"
     
    return stack.pop()
 
# Driver program to test above functions    
stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))
push(stack, str(50))
push(stack, str(60))

print(pop(stack) + " popped from stack")
print(pop(stack) + " popped from stack")
print(pop(stack) + " popped from stack")
