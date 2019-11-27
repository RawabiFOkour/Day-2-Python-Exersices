#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:22:24 2019

@author: rawabe
"""

import numpy as np
a = np.arange(20,32).reshape((3, 4))
print("Original array: \n ___________ \n")
print(a)
print("________________________________")
for x in np.nditer(a):
  print(x,end=" ")