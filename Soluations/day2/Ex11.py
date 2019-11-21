#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:11:55 2019

@author: rawabe
"""

try:
    a=3
    if a<4:
        b=a/(a-3)
    print("Value of b = " ,b)
except(ZeroDivisionError,NameError) :
    print("\nError Occurred and Haldled")
    
    
    
    
"""
//output

Error Occurred and Haldled


"""    