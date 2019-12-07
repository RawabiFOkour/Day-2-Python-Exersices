#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:30:40 2019

@author: rawabi
"""

import sqlite3
conn=sqlite3.connect('new.db')
c = conn.cursor()
c.execute('''CREATE TABLE new (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO new VALUES ('2006-01-05', 'BUY', 'RHAT', 100,35.14)")
c.execute("INSERT INTO new VALUES ('2006-01-05', 'SEL', 'RHAT', 50,35.25)")
conn.commit()
symbol = 'RHAT'
c.execute("SELECT * FROM new WHERE symbol = '%s'" % symbol)
for row in c:
    print (row)
conn.close()


