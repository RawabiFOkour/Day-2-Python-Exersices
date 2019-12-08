#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:40:57 2019

@author: rawabe
"""

from flask import Flask , render_template
app=Flask(__name__)

@app.route('/')
def index():
    return "This is the Index Page"

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/members')
def members():
    return "Members Page"

if __name__=='__main__':
    app.run(debug =True)