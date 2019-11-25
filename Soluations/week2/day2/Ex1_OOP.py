#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:40:37 2019

@author: rawabe
"""

class Employee:
    def __init__(self,Number,Name,Address,Salary,JobTitle):
        self.Number=Number
        self.__Name=Name
        self.__Address=Address
        self.__Salary=Salary
        self.__JobTitle=JobTitle
    def getName(self):
        return self.__Name
    def getAddress(self):
        return self.__Address
    def setAddress(self,Address):
        self.__Address=Address
    def getSalary(self):
        return self.__Salary
    def getJobTitle(self):
        return self.__JobTitle
    
    def __del__(self):
        print( self.__Name + " has been deleted")
    
    def Print1(self):
        print(f'''
              . Employee1 Information:
                  .Employee1 Number : {self.Number}
                  .Name : {self.__Name}
                  .Address : {self.__Address}
                  .Salary : {self.__Salary}
                  .Job Title : {self.__JobTitle}      
        ''')
    def Print2(self):
        print("Employee2 Information: Employee Number = %d , Name = %s ,Address = %s ,Salary = %d , Job Title = %s " % (self.Number,self.__Name,self.__Address,self.__Salary,self.__JobTitle) )
         
            



Employee1=Employee(1,"Mohammad Khalid","Amman,Jordan",500,"Consultant")
Employee2=Employee(2,"Hala Rana","Aqaba,Jordan",750,"Manger")



Employee1.Print1()
Employee2.Print2()

Employee1.setAddress('USA')
print(Employee1.getAddress())

del Employee1
del Employee2


    
        
    
    
        
        
       
        