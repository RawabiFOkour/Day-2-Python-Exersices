#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:29:16 2019

@author: rawabi
"""

import sqlite3
conn = sqlite3.connect('new.db')
c = conn.cursor()
c.execute('SELECT symbol, qty , price FROM new ORDER BY price')
print(c.fetchall())
conn.close()