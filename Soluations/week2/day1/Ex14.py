#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:46:45 2019

@author: rawabe
"""

import functools

lis = [ 1 , 3, 5, 6, 2,0,-4 ]
print ("The minimum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a < b else b,lis))


"""
output

The minimum element of the list is : -4

"""


