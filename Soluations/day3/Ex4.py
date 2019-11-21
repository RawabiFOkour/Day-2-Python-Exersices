#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:01:09 2019

@author: rawabe
"""
"""
firat way
"""
a = [10,20,30,20,10,50,60,40,80,50,40]
a = list(dict.fromkeys(a))
print(a)

"""
another way
"""

print(list(set(a)))