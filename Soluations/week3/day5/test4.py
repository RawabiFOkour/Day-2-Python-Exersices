#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:41:03 2019

@author: rawabi
"""

import sqlite3
conn = sqlite3.connect('new.db')
c = conn.cursor()
c.execute('UPDATE new SET qty=10000 where symbol = "RHAT"')
conn.commit()
for row in c.execute('SELECT symbol, qty, price FROM new ORDER BY price'):
    print (row)
conn.close()