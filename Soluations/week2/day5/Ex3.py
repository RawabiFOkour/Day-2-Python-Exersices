#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:25:34 2019

@author: rawabe
"""

import pandas as pd


data = [20, 10, 150, 110, 100, 50]
s = pd.Series(data)

s.plot(kind="bar")