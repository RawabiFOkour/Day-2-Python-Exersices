#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:52:36 2019

@author: rawabi
"""
from tkinter import *
from tkinter import messagebox

def act ():
    if value1.get() == "Orange" and value2.get() == "CodingAcademy" :
         z = messagebox.showinfo("Login", "Successful login")
         print (z)
         if z == "ok":
             parent.destroy()
    else:
         messagebox.showinfo("Login", "Wrong User Name or Password")
parent = Tk()
value1 = StringVar()
value2 = StringVar()
name = Label(parent, text = "Name").grid(row=0, column = 0)
e1 = Entry(parent, textvariable= value1).grid(row = 0, column =1)
password = Label(parent, text ="Password").grid(row = 1, column = 0)
e2 = Entry(parent, textvariable= value2).grid(row = 1, column =1)
submit = Button(parent, text="Submit", command= act).grid(row = 4, column = 0)
parent.mainloop()