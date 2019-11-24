#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:27:43 2019

@author: rawabe
"""

#function that filters vowels

def fun(variable):
    letters=['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False
    
    
    
sequence =['g','j','e','j','k','o','p','r']  
filtered=list(filter(fun,sequence))  
print(filtered)


"""
output

['e', 'o']

"""
