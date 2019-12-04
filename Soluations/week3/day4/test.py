#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:44:32 2019

@author: rawabi
"""

test=[1,1,1,2,3,4,2,2,3,1,4,4,4]
print(max(set(test),key=test.count))
