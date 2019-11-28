#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:23:33 2019

@author: rawabe
"""

import pandas as pd
dictionary = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print(" dictionary:")
print(dictionary)
newSeries = pd.Series(dictionary)
print("new series:")
print(newSeries)