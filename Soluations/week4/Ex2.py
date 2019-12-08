#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:45:04 2019

@author: rawabe
"""

from flask import Flask , render_template
app=Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('index1.html' , marks = score)
if __name__=='__main__':
    app.run(debug =True)
