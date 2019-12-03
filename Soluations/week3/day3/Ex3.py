#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:35:15 2019

@author: rawabi
"""
from tkinter import *
from tkinter.colorchooser import *

root = Tk()
def getcolor():
    color=askcolor()
    root.config(background=color[1])
Button(root,text="select",command=getcolor).pack()
mainloop()