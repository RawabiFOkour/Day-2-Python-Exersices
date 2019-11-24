#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:43:59 2019

@author: rawabe
"""

c=filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))
print(list(c))


"""
output

[4, 6, 8]

"""