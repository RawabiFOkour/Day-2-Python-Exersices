#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:42:16 2019

@author: rawabe
"""



number=int(input('Enter number plz ? '))

#number 10 --- show the same result 

for row in range (1,number):
    
    for space in range (1,number-row):
        print(" ", end=" ")
        
    for part1 in range (1,row):
        print(part1, end=" ")
        
    for part2 in range (row, 0, -1):
        print(part2, end=" ")
        
    print("\n")
    
    
    
    
    
for row in range (number-2,0, -1):
    
    for space in range (1,number-row):
        print(" ", end=" ")
        
    for part1 in range (1,row):
        print(part1, end=" ")
        
    for part2 in range (row, 0, -1):
        print(part2, end=" ")
        
    print("\n")

















        
    
    