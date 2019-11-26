# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:38:21 2019

@author: OJO3
"""
from functools import reduce
import math

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
        


Employee1=Employee("Ahmad Yazan","Amman,Jordan",1000,500,"HR Consultant",[432,200,1020])
Employee2=Employee("Hala Rana","Aqaba,Jordan",2000,750,"Department Manger",[150,3000,250])
Employee3=Employee("Mariam Ali","Mafraq,Jordan",3000,600,"HR S Consultant",[304,1000,250,300,500,235])  
Employee4=Employee("Yasmeen Mohammad","Karak,Jordan",4000,865,"Director",[])

# =============================================================================
# print(Employee1.getName())
# print(Employee1.getAddress())
# print(Employee1.getSalary())
# print(Employee1.getjobTitle())
# print(Employee1.getTotalLoans())
# print(Employee1.getMaxLoans())
# print(Employee1.getMinLoans())
# print(Employee1.setLoans(5))
# Employee1.printInfo()
# =============================================================================

Student1=Student("Khalid Ali","Irbid,Jordan",20191000,"History",{"English":80,"Arabic":90,"Art":95,"Management":75})
Student2=Student("Reem Hani","Zarqa,Jordan",20182000,"Software Eng",{"English":80,"Arabic":90,"Management":75,"Calculus":85,"OS":73,"Programming":90})
Student3=Student("Nawras Abdullah","Amman,Jordan",20161001,"Arts",{"English":83,"Arabic":92,"Atr":90,"Management":70})
Student4=Student("Amal Raed","Tafelah,Jordan",20172030,"Computer Eng",{"English":83,"Arabic":92,"Management":70,"Calculus":80,"OS":79,"Programming":91}) 
# =============================================================================
# print(Student1.getName())
# print(Student1.getAddress())
# print(Student1.getSubject())
# print(Student1.getMarks())
# print(Student1.average())
# print(Student1.getAMarks())1
# Student1.studentInfo()
# =============================================================================

#Ex1:
employeeList = [Employee1,Employee2,Employee3,Employee4]

#Ex2:
studentList = [Student1,Student2,Student3,Student4]

#Ex3:
# =============================================================================
# print("The total number of employees: ", len(employeeList))
# =============================================================================

#Ex4:
# =============================================================================
# print("The total number of students: ",len(employeeList))
# =============================================================================

#Ex5:
# =============================================================================
# for employee in (employeeList):
#     employee.printInfo()
#     print("_______________________")
# =============================================================================
    
#Ex6:
# =============================================================================
# for student in (studentList):
#     student.studentInfo()
#     print("_______________________")
# =============================================================================
    
#Ex7:

# =============================================================================
# maxAll = 0
# for student in (studentList):
#     if ( maxAll <= student.average()):
#         maxAll = student.average()
# print (maxAll)
# =============================================================================

#Ex8:
# =============================================================================
# mini = math.inf
# 
# for emp in (employeeList):
#     if len(emp.getLoans()) == 0:
#         continue
#     if emp.getMinLoans()<mini:
#         mini = emp.getMinLoans()
# 
# print(mini)
# =============================================================================

#Ex9:
# =============================================================================
# maxi = 0
# for emp in (employeeList):
#     if len(emp.getLoans()) == 0:
#         continue
#     if emp.getMinLoans()>maxi:
#         maxi = emp.getMaxLoans()
# 
# print(maxi)
# =============================================================================

#Ex10:
# =============================================================================
# sumAll = 0
# for emp in employeeList:
#     print(emp.getName(), end =": ")
#     if(len(emp.getLoans()) == 0):
#         print("have no loans")
#         continue
#     print ("Loans:", emp.getLoans())
#     print ("Total Loans", emp.getTotalLoans())
#     sumAll = sumAll + emp.getTotalLoans()
# 
# print("Grand total for all employees: ", sumAll)
# =============================================================================

#EX11:

# =============================================================================
# for emp in employeeList:
#     print({str(emp.employeeNumber): emp.getLoans()})
#     print("_______")
# =============================================================================

#EX12:

# =============================================================================
# for emp in employeeList:
#     print(emp.getName(), end = ": ")
#     if(len(emp.getLoans()) == 0):
#         print("have no loans")
#     else:
#         print ("min:" , reduce(lambda a,b : a if a<b else b, emp.getLoans()))
#         print ("max:" , reduce(lambda a,b : a if a>b else b, emp.getLoans()))
# =============================================================================
#EX13:
# =============================================================================
# for n in studentList:
#     if(len(n.getAMarks()) == 0):
#         continue
#     n.studentInfo()
#     print("________")
# =============================================================================

#EX14:
# =============================================================================
# maxSalary = 0
# for emp in (employeeList):
#       if emp.getSalary()>maxSalary:
#         maxSalary = emp.getSalary()
# 
# print("maxSalary",maxSalary)
# =============================================================================

#EX15:
# =============================================================================
# minSalary = math.inf
# for emp in (employeeList):
#    
#     if emp.getSalary()<minSalary:
#         minSalary = emp.getSalary()
# 
# print("minSalary", minSalary)
# =============================================================================

#EX16:
# =============================================================================
# Total=0
# for n in employeeList:
#     Total= n.getSalary()+Total
# print(Total)
# =============================================================================

#EX17:
print("Test Delete")
del employeeList
del studentList

del Student1, Student2, Student3, Student4, Employee1, Employee2, Employee3, Employee4 

    
