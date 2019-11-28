#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:20:21 2019

@author: rawabe
"""
import pandas as pd
Data = {'d1':[100,200,5,400,700,100,200,50,400,700],'d2':[140,0,300,400,200,140,0,700,400,200]  }
s = pd.DataFrame(Data)
s.plot()