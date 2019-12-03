#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:41:02 2019

@author: rawabi
"""
import tkinter as tk
from tkinter import *
# =============================================================================
# root = Tk(className="My first GUI")
# 
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# 
# print("Screen width" , screen_width)
# print("Screen width" , screen_height)
# 
# screen_width2=screen_width/2
# screen_height2=screen_height/2
# print(screen_width2)
# print(screen_height2)
# root.geometry("300x150+383+384")
# =============================================================================
# =============================================================================
# root.geometry("300x150+50+50")
# =============================================================================


# =============================================================================
# root = tk.Tk()
# 
# label =tk.Label(root,text="Hello World", font=('times',20,'bold') ,padx=10,pady=10)
# 
# label.pack()
# 
# =============================================================================

# =============================================================================
# 
# root=Tk()
# root.geometry("200x100")
# b=Button(root,text="Simple")
# b2=Button(root,text="Simple2")
# b.pack(side=LEFT ,padx=7)
# b2.pack(side=LEFT ,padx=7)
# =============================================================================

# =============================================================================
# 
# root=Tk()
# frame = Frame(root)
# frame.pack()
# bottomframe=Frame(root)
# bottomframe.pack(side=BOTTOM)
# red=Button(frame,text="Red",fg="red")
# red.pack(side=LEFT)
# =============================================================================


# =============================================================================
# def ClickMe():
#     print("Hello , Press me again")
#     
# root=Tk()
# b=Button(root,text="Press me",fg="red" ,command=ClickMe)
# b.pack(pady=40,padx=40)
# =============================================================================

from tkinter import messagebox
# =============================================================================
# def ClickMe():
#     title='please answer'
#     text='Do you Like to travel?'
#     answer=messagebox.askquestion(title,text)
#     if answer == 'yes':
#         print('i like this ?')
#     else:
#         print('you must have clicked the wrong button by accident')
#     
# root=Tk()
# b=Button(root,text="Press me",fg="red" ,command=ClickMe)
# b.pack(pady=40,padx=40)
# 
# =============================================================================


# =============================================================================
# root =Tk()
# v=StringVar()
# e=Entry(root,textvariable=v)
# e.pack()
# v.set("orange academy")
# print(v.get())
# =============================================================================

# =============================================================================
# from tkinter import *
# root=Tk(className="My first GUI")
# svalue=StringVar()
# w=Entry(root,textvariable=svalue)
# w.pack()
# def act():
#     print("you entered")
#     print('%s' % svalue.get())
# foo=Button(root,text='Press me :p',command=act)
# foo.pack()
# root.mainloop()
# 
# =============================================================================

# =============================================================================
# 
# root = Tk()
# root.title('menu_win')
# def notdone():
#     messagebox.showinfo('Not implemented', 'Not yet available')
# top = Menu(root)
# root.config(menu=top)
# file = Menu(top,tearoff=0)
# file.add_command(label='New...', command=notdone)
# file.add_command(label='Open...', command=notdone)
# file.add_separator()
# file.add_command(label='Quit', command=root.destroy)
# top.add_cascade(label='File', menu=file)
# edit = Menu(top,tearoff= 0)
# edit.add_command(label='Cut', command=notdone)
# edit.add_command(label='Paste', command=notdone)
# top.add_cascade(label='Edit', menu=edit)
# root.mainloop()
# =============================================================================


from tkinter.colorchooser import *
def getColor():
    color = askcolor()
    print (color)
Button(text='Select Color', command=getColor).pack()
mainloop()
















root.mainloop()