#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:10:01 2019

@author: rawabi
"""

from xlrd import open_workbook
wb=open_workbook('rawabi.xlsx')

for s in wb.sheets():
    print('Sheet:',s.name)
    for row in range(s.nrows):
        values=[]
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(','.join(values))