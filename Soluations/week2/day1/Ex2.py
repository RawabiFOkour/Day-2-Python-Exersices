#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:03:26 2019

@author: rawabe
"""
from functools import reduce
list=[1,3,5,2]
result=reduce(lambda a,b :a*b ,list)
print(result)