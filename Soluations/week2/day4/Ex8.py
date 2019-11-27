#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:34:41 2019

@author: rawabe
"""

import numpy as np
Vector1 = np.array([1, 8, 3, 5])
print("Vector1")
print(Vector1)
Vector2= np.random.randint(0, 11, 4)
print("Vector2")
print(Vector2)
result = Vector1 * Vector2
print("Multiply the values of two said vectors:")
print(result)