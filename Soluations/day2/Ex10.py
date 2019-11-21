#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:03:27 2019

@author: rawabe
"""

while True:
  try:
    n = int(input("Please enter an integer: "))
    break


  except ValueError:
    print("No valid integer! Please try again .")
print(" successfully entered an integer!")