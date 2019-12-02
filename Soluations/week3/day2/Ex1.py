#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:24:49 2019

@author: rawabi
"""


from sympy import *
from sympy.plotting import *
x,y,z = symbols('x y z')
print("____________________")
expr= x**2+x**3+21*x**4 + 10*x+1
print( expr.subs(x, 7) )
print("____________________")
print(expand( (x + y) ** 2))
print("____________________")
print(simplify(4*x**3+21*x**2+10*x+12))
print("____________________")
print(limit(1/(x**2),x,oo))
print("____________________")
print(integrate(sin(x)+exp(x)*cos(x)+tan(x),x))
print("____________________")
print(factor(x**3 + 12*x*y*z +3*y**2*z) )
print("____________________")
print(solveset(x-4,x))
print("____________________")
m1 =Matrix([[5, 12, 40], [30, 70, 2]])
m2 =Matrix([2, 1, 0])
print( m1*m2 )
print("____________________")
plot(x**3+3, (x, -10, 10))
print("____________________")
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))