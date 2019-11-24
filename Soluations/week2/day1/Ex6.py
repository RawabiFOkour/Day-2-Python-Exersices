#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:21:29 2019

@author: rawabe
"""

x=("Joey","Monica","Ross")
y=("Chandler","Pheobe","Ross")
z=("david","Rachel","Courtney")
result=list(zip(x,y,z))
print(result)


"""
output

[('Joey', 'Chandler', 'david'), ('Monica', 'Pheobe', 'Rachel'), ('Ross', 'Ross', 'Courtney')]

"""