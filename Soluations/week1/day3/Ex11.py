#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:48:27 2019

@author: rawabe
"""

dic1={1:10,2:20}
dic2={1:10,2:20}
dic3={1:10,2:20}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)


"""
________output__

{1: 10, 2: 20}
"""