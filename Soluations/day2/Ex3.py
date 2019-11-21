#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:57:13 2019

@author: rawabe
"""

number=5;
for row in range(number):
    for col in range(row):
        print ('* ', end="")
    print('')

for row in range(number,0,-1):
    for col in range(row):
        print('* ', end="")
    print('')