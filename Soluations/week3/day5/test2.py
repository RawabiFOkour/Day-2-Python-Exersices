#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:06:31 2019

@author: rawabi
"""
import sqlite3
conn=sqlite3.connect('new.db')
c = conn.cursor()
c.execute("INSERT INTO new VALUES ('2006-01-05', 'BUY', 'APPLE', 100,4.49)")
c.execute("INSERT INTO new VALUES ('2006-01-05', 'SEL', 'APPLE', 50,3.23)")
c.execute("INSERT INTO new VALUES ('2006-01-05', 'BUY', 'APPLE', 100,4.49)")
c.execute("INSERT INTO new VALUES ('2006-01-05', 'SEL', 'APPLE', 50,3.23)")
conn.commit()
conn.close()