#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:06:27 2019

@author: rawabe
"""
import pandas as pd
import numpy as np

dates =pd.date_range('20000101', periods=4)
df= pd.DataFrame(np.random.randn(4, 2), index=dates, columns=["A","B"])
print(df)
print("----------------------------------------")
print(df.head(2))
print("----------------------------------------")

print(df[['A']])
print("----------------------------------------")

print(df[0:1]) 
print("----------------------------------------")

print(df['20000102':'20000104'])
print("----------------------------------------")

print(df.loc['20000102':'20000104', ["A"]])
print("----------------------------------------")

print(df.iloc[:,1:2])
print("----------------------------------------")

print(df[df>0])
print("----------------------------------------")

print(df[df.B>0])
print("----------------------------------------")

df["A"]=[100,200,300,100]
print(df)
print("----------------------------------------")

print(df[df['A'].isin([200,300])])