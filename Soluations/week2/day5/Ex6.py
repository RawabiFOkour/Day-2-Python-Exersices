#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:46:12 2019

@author: rawabe
"""


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

series = pd.Series(births, index=names, name='series')

series.plot.pie(y='births', figsize=(5, 5))


