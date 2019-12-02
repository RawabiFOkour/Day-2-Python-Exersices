#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:27:47 2019

@author: rawabi
"""

import xlsxwriter
workbook = xlsxwriter.Workbook('write.xlsx')
worksheet = workbook.add_worksheet()
worksheet.autofilter('A1:B1')
data = ["this is example"]
format = workbook.add_format()
format.set_font_color('red')
format.set_font_size(12)
worksheet.write_column('A1:B1', data ,format)
data2 = ["export my sheet"]
format = workbook.add_format()
format.set_font_color('black')
format.set_font_size(12)
worksheet.write_column('A2:B2', data2 ,format)
data3=[1,2]
data4=[3]
for elem in data3:
    format = workbook.add_format()
    format.set_font_color('black')
    format.set_font_size(12)
    worksheet.write_column("A3:A4", data3 ,format)
for elem in data4:
    format = workbook.add_format()
    format.set_font_color('red')
    format.set_font_size(12)
    worksheet.write_column("A5", data4 ,format)
workbook.close()

