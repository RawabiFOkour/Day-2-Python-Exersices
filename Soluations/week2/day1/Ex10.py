#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:34:57 2019

@author: rawabe
"""

def newfunc(a):
    return a*a
x=list(map(newfunc,(1,2,3,4)))
print(x)


"""
output


[1, 4, 9, 16]


"""