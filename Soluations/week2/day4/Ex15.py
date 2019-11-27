#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:57:13 2019

@author: rawabe
"""

import matplotlib.pyplot as plt

x = ['Python', 'Java', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
xpostion = [i for i, _ in enumerate(x)]
plt.bar(xpostion, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language")
plt.xticks(xpostion, x)
plt.show()
