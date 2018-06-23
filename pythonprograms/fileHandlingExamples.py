# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:17:49 2018

@author: lakshmi
"""
import os
import sys

#scriptpath = "D:\lakshmi\projects\PythonExamples"

# Add the directory containing your module to the Python path (wants absolute paths)
#sys.path.append(os.path.abspath(scriptpath))
handle = open("python-logo.gif", "rb")
while True: 
	data = handle.read(1024) 
	print(data) 
	if not data: 
		break 

#Program to copy an image from one file to another

f1 = open("python-logo.gif", "rb")
f2 = open("newpython-logo.gif", "wb")
#Read bytes from f1 and write into f2
bytes = f1.read()
f2.write(bytes)

#close the files
f1.close()
f2.close()