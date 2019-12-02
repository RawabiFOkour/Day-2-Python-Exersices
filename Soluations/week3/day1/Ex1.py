#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:05:57 2019

@author: rawabi
"""
import statistics as st
x=[3,1.5,4.5,6.75,2.25,5.75,2.25]
print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))