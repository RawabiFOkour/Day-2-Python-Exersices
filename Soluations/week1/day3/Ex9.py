#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:44:16 2019

@author: rawabe
"""

setx=set(["green","blue"])
sety=set(["green","yellow"])
seta= setx | sety
print(seta)

"""
___________output__________


{'yellow', 'blue', 'green'}

"""