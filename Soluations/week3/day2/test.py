#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:39:15 2019

@author: rawabi
"""
# =============================================================================
# import sympy as sym
# x = sym.symbols('x')
# expr = x + 1
# print ( expr.subs(x, 2) )
# 
# =============================================================================

# =============================================================================
# import sympy as sym
# x = sym.symbols('x')
# expr = x + x**2 + 1
# print ( expr.subs(x, 2) )
# =============================================================================


# =============================================================================
# import sympy as sym
# x, y, z = sym.symbols('x y z')
# expr = x**3 + 4*x*y - z
# print( expr.subs([(x, 2), (y, 4), (z, 0)]) )
# =============================================================================

# =============================================================================
# from sympy import *
# x = symbols('x')
# str_expr = "x**2 + 3*x - 1/2"
# expr = sympify(str_expr)
# 
# print ( expr)
# print ( expr.subs(x, 2))
# =============================================================================


# =============================================================================
# from sympy import *
# x = symbols('x')
# init_printing()
# expr = Integral(sqrt(1/x),x)
# print (expr)
# pprint (expr)
# =============================================================================

# =============================================================================
# from sympy import *
# x = symbols('x')
# init_printing()
# expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
# print (expr)
# =============================================================================

# =============================================================================
# 
# import sympy as sym
# x = sym.Symbol('x')
# y, i ,n, a, b = sym.symbols('y i n a b')
# 
# 
# f = x**2 + 1
# print( f.subs(x, 2))
# 
# print(
# sym.expand( (x + y) ** 4 ))
# 
# print( sym.simplify((x + x * y) / x))
# 
# 
# print(sym.limit(sym.sin(x) / x, x, 0))
# 
# 
# =============================================================================


# =============================================================================
# from sympy import symbols
# from sympy.plotting import plot
# x = symbols('x')
# 
# plot(x**2, (x, -5, 5))
# =============================================================================


# =============================================================================
# from sympy import symbols
# from sympy.plotting import plot3d
# x, y = symbols('x y')
# f=x**2*y**2
# plot3d(f, (x, -5, 5), (y, -5, 5))
# =============================================================================


# =============================================================================
# 
# from sympy import symbols
# from sympy.plotting import plot3d
# x, y = symbols('x y')
# f=cos(x)+sin(y)
# plot3d(f, (x, -10, 10), (y, -10, 10))
# =============================================================================

import xlsxwriter

workbook = xlsxwriter.Workbook('example10.xlsx')
worksheet=workbook.add_worksheet()

worksheet.autofilter('A1:B4')
data=["Test",10,40,50,20]
format=workbook.add_format()
format.set_bold()
format.set_font_color('red')
format.set_font_size(20)

worksheet.write_column('A1',data,format)

worksheet.write_column('B1','This is a comment')

format2 = workbook.add_format({'bold':True,'font_color':'blue'})

worksheet.write_column('B1',data,format2)

workbook.close()






























