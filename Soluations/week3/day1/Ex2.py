#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:08:33 2019

@author: rawabi
"""


import random
print( random.random() )
print ( random.randrange(10) )
print ( random.choice(['Ali', 'Khalid', 'Hussam']) )
print ( random.sample(range(1000), 10) )
print ( random.choice('OrangeAcademy') )
items = [1,5,8,9,2,4]
random.shuffle(items)
print( items )
print ( random.randint(20,30) )
print ( random.randrange(1000, 2111, 5) )
print  ( random.uniform(10000, 1100))
