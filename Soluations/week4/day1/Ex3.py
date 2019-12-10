#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:02:38 2019

@author: rawabe
"""

from flask import Flask , render_template
app=Flask(__name__)

@app.route('/index')
def index():
    return render_template('Q3.html')
if __name__=='__main__':
    app.run(debug =True)