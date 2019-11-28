#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:58:19 2019

@author: rawabe
"""
import pandas as pd
d = [100,2200,300,400,500,600,700,800,900]
df = pd.DataFrame(d, columns = ['Number'])

df.to_csv('myDataFrame.csv', sep='\t')

df =pd.read_csv('myDataFrame.csv',sep='\t',index_col=0)
print(df)
print("_______________________________")
df =pd.read_csv('myDataFrame.csv',sep=',',index_col=0)
print(df)