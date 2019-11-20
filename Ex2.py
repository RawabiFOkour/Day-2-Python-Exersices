#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:28:40 2019

@author: rawabe
"""
number=int(input('input number ?  '))
n=1
for n in range(1,11):
    
    print(str(number) + "*" + str(n) + "=" + str(number * n))