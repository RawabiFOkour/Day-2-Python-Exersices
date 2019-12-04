#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:46:38 2019

@author: rawabi
"""


from tkinter import *
from functools import reduce
from tkinter import scrolledtext
from tkinter import messagebox
import math
import json
employeesList = []
studentList = []

class Person:
    def __init__(self,name,address):
        self._name=name
        self._address=address
    def getName(self):
        return  self._name
    def setName(self,name):
         self._name=name
    def getAddress(self):
        return self._address
    def setAddress(self,address):
        self._address=address
    def __del__():
        print("I have been deleted")



class Employee (Person):
    def __init__(self, name:str, address:str, employeeNumber:int, salary:float, jobTitle:str, loans:list):
        super().__init__(name,address)
        self.employeeNumber= employeeNumber
        self.__salary = salary
        self.__jobTitle=jobTitle
        self.__loans= loans
    def getSalary(self):
        return self.__salary
    def setSalary(self, newSalary):
        self.__salary= newSalary
    def getjobTitle(self):
        return self.__jobTitle
    def setjobTitle(self, jobTitle):
        self.__jobTitle= jobTitle
    def getTotalLoans(self):
        return sum(self.__loans)
    def getLoans(self):
        return self.__loans
    def getMaxLoans(self):
        return max(self.__loans)
    def getMinLoans(self):
        return min(self.__loans)
    def setLoans(self, newLoan):
        return self.__loans.append(newLoan)
    def printInfo(self):
        print('Employee Name', self.getName())
        print('Employee Address', self.getAddress())
        print('Employee Number', self.employeeNumber)
        print('Salary: ', self.__salary)
        print('Job Title: ',self.__jobTitle)
        print('Loans: ', self.__loans)
        print('Total: ', self.getTotalLoans())
    def __del__( self ):
        print ( 'I have been deleted')



class Student (Person):
    def __init__(self, name, address, studentNumber, subject, marks):
          super().__init__( name, address)
          self.studentNumber=int(studentNumber)
          self.__subject=str(subject)
          self.__marks=dict(marks)
    def getSubject (self):
        return self.__subject
    def setSubject (self, newSubject):
        self.__subject = newSubject
    def getMarks (self):
        return self.__marks
    def setMarks (self, newMarks):
        self.__marks = newMarks
    def average (self):
        return reduce(lambda a,b: a+b, self.__marks.values()) / len(self.__marks)
    def getAMarks (self):
        return list(filter(lambda x: x>=90, self.__marks.values()))
    def studentInfo (self):
        print('Student Name', self.getName())
        print('Student Address', self.getAddress())
        print('Student Number', self.studentNumber)
        print('Student Subject', self.__subject)
        print('Student Marks: ', self.__marks)
        print('Student Avg: ', self.average())
    def __del__( self ):
        print ( 'I have been deleted')

root= Tk(className="Project 2")

sw= root.winfo_screenwidth();
sh= root.winfo_screenheight();
x=int((sw-500)/2)
y=int((sh-500)/2)
g= "500x500+"+str(x)+"+"+str(y)
root.geometry(g)


    
def addEmployee () :
    c =Toplevel(root)
    c.title("Add Employee")
    ae= "300x130+"+str(x+100)+"+"+str(y+100)
    c.geometry(ae)
    Label(c,text =" Name ").grid(row=0, column=0)
    nValue=StringVar()
    Name = Entry(c, textvariable = nValue).grid(row=0, column=1)
    
    Label(c,text =" Address ").grid(row=1, column=0)
    aValue=StringVar()
    Address = Entry(c, textvariable = aValue).grid(row=1, column=1)
    
    Label(c,text =" Employee Num ").grid(row=2, column=0)
    enValue=StringVar()
    EmployeeNum = Entry(c, textvariable = enValue).grid(row=2, column=1)
    
    Label(c,text =" Salary ").grid(row=3, column=0)
    sValue=StringVar()
    Salary = Entry(c,textvariable=sValue).grid(row=3, column=1)
    
    Label(c,text =" Job Title ").grid(row=4, column=0)
    jValue=StringVar()
    JobTitle = Entry(c,textvariable=jValue).grid(row=4, column=1)
    
    Label(c,text =" Loans ").grid(row=5, column=0)
    lValue=StringVar()
    Loans = Entry(c,textvariable=lValue).grid(row=5, column=1)
    
    b = Button(c, text="Add!", command=lambda:saveEmployee(nValue.get(),aValue.get(),enValue.get(),sValue.get(),jValue.get(),lValue.get()))
    b.grid(row=6, column=1)
    
def saveEmployee(name, address, employeeNumber, salary, jobTitle, loans):
    global employeesList
    salary = float(salary)
    loans =  [int(i) for i in loans.split(",")]
    name = str(name)
    print (name,address, employeeNumber, salary, jobTitle, loans)
    employeesList.append(Employee(name,address,employeeNumber,salary,jobTitle,loans))
    print(employeesList[0].getName())
    Title='Add'
    Text='Addeded Successfully'
    ans= messagebox.showinfo(Title, Text)
    
def addStudent () :
    c =Toplevel(root)
    c.title("Add Student")
    ae= "300x120+"+str(x+100)+"+"+str(y+100)
    c.geometry(ae)
    Label(c,text =" Name ").grid(row=0, column=0)
    nValue=StringVar()
    Name = Entry(c, textvariable=nValue).grid(row=0, column=1)
    
    Label(c,text =" Address ").grid(row=1, column = 0)
    aValue=StringVar()
    Address = Entry(c, textvariable=aValue).grid(row=1, column=1)
    
    Label(c,text =" Student Num ").grid(row=2, column=0)
    snValue=StringVar()
    StudentNum = Entry(c, textvariable=snValue).grid(row=2, column=1)
    
    Label(c,text =" Subject ").grid(row=3, column=0)
    subjValue=StringVar()
    Subject = Entry(c, textvariable=subjValue).grid(row=3, column=1)
    
    Label(c,text =" Marks ").grid(row=4, column=0)
    mValue=StringVar()
    Marks = Entry(c, textvariable=mValue).grid(row=4, column=1)
    
    
    b = Button(c, text="Add!", command=lambda:saveStudent(nValue.get(),aValue.get(),snValue.get(),subjValue.get(),mValue.get()))
    b.grid(row=6, column=1) 

def saveStudent(name, address, studentNumber, subject, marks):
    global studentList
    print (name, address, studentNumber, subject, marks)
    newMarks =  [int(i) for i in marks.split(",")]
    marksWithSub = {"English":newMarks[0],"Arabic":newMarks[1]}
    studentList.append(Student(name,address,studentNumber,subject,marksWithSub))
    print(studentList[0].getMarks())
    Title='Add'
    Text='Addeded Successfully'
    ans= messagebox.showinfo(Title, Text)
    

def viewEmployee ():
    c =Toplevel(root)
    c.title("View Employee")
    ae= "300x300+"+str(x+100)+"+"+str(y+100)
    c.geometry(ae)
# =============================================================================
#     txt = scrolledtext.ScrolledText(c, width=200, height=200, wrap=WORD)
#     for emp in employeesList:
#         txt.insert(END, emp.printInfo())
#     txt.yview(END)
#     txt.pack()
# =============================================================================
    txt = scrolledtext.ScrolledText(c, width=200, height=200, wrap=WORD)
    for emp in employeesList:
        txt.insert(END, "name: "+emp.getName() + "\n")
        
        txt.insert(END, "address: "+emp.getAddress()+ "\n")
        
        txt.insert(END, "salary: "+str(emp.getSalary()) + "\n")
        
        txt.insert(END, "job: "+str(emp.getjobTitle())+ "\n")
        
        txt.insert(END, "loans: "+str(emp.getLoans())+ "\n")
        
        txt.insert(END, "________________ \n")
    txt.yview(END)
    txt.pack()
# =============================================================================
#     for emp in employeesList:
#         Label(c, text="name: "+emp.getName()).pack()
#         
#         Label(c, text="address: "+emp.getAddress()).pack()
#         
#         Label(c, text="salary: "+str(emp.getSalary())).pack()
#         
#         Label(c, text="job: "+str(emp.getjobTitle())).pack()
#         
#         Label(c, text="loans: "+str(emp.getLoans())).pack()
#         
#         Label(c, text="________________").pack()
# =============================================================================

def viewStudent ():
    c =Toplevel(root)
    c.title("View Employee")
    ae= "300x300+"+str(x+100)+"+"+str(y+100)
    c.geometry(ae)
    txt = scrolledtext.ScrolledText(c, width=200, height=200, wrap=WORD)
    for st in studentList:
        txt.insert(END,  "name: "+st.getName() + "\n")
        
        txt.insert(END,  "address: "+st.getAddress() + "\n")
        
        txt.insert(END, "subject: "+st.getSubject() + "\n")
        
        txt.insert(END,  "marks: "+str(st.getMarks()) + "\n")
        
        txt.insert(END,  "avg: "+str(st.average()) + "\n")
        
        txt.insert(END,  "________________ \n")
    txt.yview(END)
    txt.pack()
# =============================================================================
#     for st in studentList:
#         Label(c, text="name: "+st.getName()).pack()
#         
#         Label(c, text="address: "+st.getAddress()).pack()
#         
#         Label(c, text="subject: "+st.getSubject()).pack()
#         
#         Label(c, text="marks: "+str(st.getMarks())).pack()
#         
#         Label(c, text="avg: "+str(st.average())).pack()
#         
#         Label(c, text="________________").pack()
# =============================================================================

def deleteEmployee() :
    global employeesList
    c =Toplevel(root)
    c.title("Add Student")
    ae= "300x70+"+str(x+100)+"+"+str(y+100)
    c.geometry(ae)
    Label(c,text =" Employee Number ").grid(row=0, column=0)
    Value=IntVar()
    Number = Entry(c, textvariable=Value).grid(row=0, column=1)
    b = Button(c, text="Delete!", command=lambda: d(Value.get()))
    b.grid(row=1, column=1)
    
    
def d (Value):
    print (type(Value))
    global employeesList
    print(type(employeesList[0].employeeNumber))
    test = list(filter(lambda x: int(x.employeeNumber) == Value, employeesList))
    employeesList = test
    Title='Delete'
    Text='Deleted Successfully'
    ans= messagebox.showinfo(Title, Text)
    
def deleteStudent() :
    global studentList
    c =Toplevel(root)
    c.title("Add Student")
    ae= "300x70+"+str(x+100)+"+"+str(y+100)
    c.geometry(ae)
    Label(c,text =" Student Number ").grid(row=0, column=0)
    Value=IntVar()
    Number = Entry(c, textvariable=Value).grid(row=0, column=1)
    b = Button(c, text="Delete!", command=lambda: f(Value.get()))
    b.grid(row=1, column=1)


def f (Value):
    print (type(Value))
    global studentList
    print(type(studentList[0].studentNumber))
    test = list(filter(lambda x: int(x.studentNumber) == Value, studentList))
    studentList = test
    Title='Delete'
    Text='Deleted Successfully'
    ans= messagebox.showinfo(Title, Text)

label1=Label(root,text="Welcome",font=('times',30,'bold'),padx=10,pady=10)
label2=Label(root,text=" to ",font=('times',30,'bold'),padx=10,pady=10)
label3=Label(root,text="Orange Coding Academy",font=('times',30,'bold'),padx=10,pady=10)
label1.pack(pady=50, padx=50)
label2.pack(pady=50, padx=50)
label3.pack(pady=50, padx=50)

def maxLoan(employeeList) :
     maxi = 0
     for emp in (employeeList):
        if len(emp.getLoans()) == 0:
                continue
        if emp.getMaxLoans()>maxi:
                maxi = emp.getMaxLoans()
     return maxi;
 
def minLoan(employeeList) :
    mini = math.inf

    for emp in (employeeList):
        if len(emp.getLoans()) == 0:
            continue
        if emp.getMinLoans()<mini:
            mini = emp.getMinLoans()
    return mini

def report() :
    global studentList
    global employeesList
    c =Toplevel(root)
    c.title("report")
    ae= "300x300+"+str(x+100)+"+"+str(y+100)
    c.geometry(ae)
    txt = scrolledtext.ScrolledText(c, width=200, height=200, wrap=WORD)
    txt.insert(END,  "The Employees Report: \n")
    txt.insert(END,  "The total number of employees: "+str(len(employeesList)) + "\n")
    txt.insert(END,  "The total number of students: "+str(len(studentList)) + "\n")
    txt.insert(END,  "The max loan: "+str(maxLoan(employeesList)) + "\n")
    txt.insert(END,  "The min loan: "+str(minLoan(employeesList)) + "\n")
    txt.yview(END)
    txt.pack()
    
    

def helpMsg():
    Title='About'
    Text='OOP second Project'
    ans= messagebox.showinfo(Title, Text)
    
top = Menu(root)
root.config(menu=top)
file = Menu(top,tearoff=0)
file.add_command(label='Report', command=report)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)
top.add_cascade(label='File', menu=file)

Employees = Menu(top,tearoff= 0)
Employees.add_command(label='Add', command=addEmployee)
Employees.add_command(label='View', command=viewEmployee)
Employees.add_command(label='Delete', command=deleteEmployee)
top.add_cascade(label='Employees', menu=Employees)

Students = Menu(top,tearoff= 0)
Students.add_command(label='Add', command=addStudent)
Students.add_command(label='View', command=viewStudent)
Students.add_command(label='Delete', command=deleteStudent)
top.add_cascade(label='Students', menu=Students)

Help = Menu(top,tearoff= 0)
Help.add_command(label='About', command=helpMsg)
top.add_cascade(label='Help', menu=Help)

root.mainloop()