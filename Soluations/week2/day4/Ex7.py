#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:26:28 2019

@author: rawabe
"""

import numpy as np
x = np.arange(20)
print("Original vector:\n______________________\n")
print(x)
print("______________________________")
print("After changing the sign of the numbers in the range from 9 to 15:\n ____________________________ \n")
x[(x >= 9) & (x <= 15)] *= -1
print(x)