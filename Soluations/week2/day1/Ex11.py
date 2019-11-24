#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:36:46 2019

@author: rawabe
"""

def func(a,b):
    return a+b
a=list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)


"""
output


[3, 6, 8]


"""