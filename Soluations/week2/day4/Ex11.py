#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:00:31 2019

@author: rawabe
"""

import numpy as np
a=np.array([9,-1,2,5])
b=np.array([1,-6,0,10])
c=np.array([[1,8,2,5],[3,1,7,9]])


print("a-b:",a-b)
print("a*b:",a*b)
print("a.dot(b):",a.dot(b))
print("a*2:",a*2)
print("np.sin(a):",np.sin(a))
print("a<3:",a<3)
print("a.sum():",a.sum())
print("a.sum(axis=0):",a.sum(axis=0))
print("c.sum():",c.sum())
print("c.sum(axis=0):",c.sum(axis=0))
print("a.min():",a.min())
print("a.max():",a.max())
print("a.mean():",a.mean())
print("a.average():",np.average(a))
print("a.median():",np.median(a))
print("a.std():",np.std(a))
print("a.var()",np.var(a))
print("c.cumsum():",c.cumsum())
print("a[1:2]:",a[1:2])
print("a[2:]:",a[2:])
print("c[-1]:",c[-1])