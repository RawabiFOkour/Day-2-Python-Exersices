#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:13:28 2019

@author: rawabe
"""

letters=["x","y","z","a","b","c"]
for i in letters :
    if i == "a":
        continue
    elif i == "c":
        break
    print (i)
    
    
"""
output

x
y
z
b


"""