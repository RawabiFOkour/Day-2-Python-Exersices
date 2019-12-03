#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:30:51 2019

@author: rawabi
"""
from tkinter import *
from tkinter import messagebox
def open_child1():
    dialog_title=""
    dialog_text="This is a message"
    answer=messagebox.showinfo(dialog_title,dialog_text)
def open_child2():
    top=Tk()
    top.title('Child window 2')
    top.geometry('400x250')
    name=Label(top,text="Emy Number").place(x=30,y=50)
    email=Label(top,text="Emy Name").place(x=30,y=90)
    e1=Entry(top).place(x=100,y=50)
    e2=Entry(top).place(x=100,y=90)
    button=Button(top,text="Quit",command=top.destroy).place(x=150,y=150)
    button.pack()
    top.mainloop()
def open_child3():
    win=Tk()
    win.title("Welcome")
    win.geometry('350x200')
    txt=scrolledtext.ScrolledText(win,width=40,height=10)
    txt.grid(column=0,row=0)
    for r in range(20):
        print(' ')
    win.mainloop()
root = Tk()
root.title('Root window')
Button(root, text = 'open child window 1', command = open_child1).grid()
Button(root, text = 'open child window 2', command = open_child2).grid()
Button(root, text = 'open child window 3', command = open_child3).grid()
root.mainloop()