# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 21:24:17 2018

@author: lakshmi
"""

f1 = open("figpath.png", "rb")
f2= open("figpathnew.png", "wb")
#Read bytes from f1 and write into f2
bytes = f1.read()
f2.write(bytes)

#close the files
f1.close()
f2.close()
