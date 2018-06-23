# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 19:50:44 2018

@author: lakshmi
"""
filename = input ("Enter name of input file: ")
fh = open (filename, "r")
str = fh.read() 
print("Read String is : ", str )
fh.close()

#f =open("Msftstock.png",'r+b')
#imgdata = f.read()
#print(imgdata)
##im.show(imgdata)
#f.close()

with open("test.txt",'a') as f: 
    f.write("my third file\n") 
#    f.write("This file\n\n") 
#    f.write("contains three lines\n") 
