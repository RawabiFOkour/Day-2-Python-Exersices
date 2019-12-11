#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:43:02 2019

@author: owner
"""
from flask import *
import sqlite3

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index25.html");
@app.route("/add")
def add():
    return render_template("add25.html")
@app.route("/savedetails",methods=['POST',"GET"])
def saveDetailes():
    msg="msg"
    if request.method=='POST' :
       try:
            name=request.form["name"]
            email=request.form["emaill"]
            address=request.form["address"]
            with sqlite3.connect("employee.db") as con :
                cur=con.cursor()
                cur.execute("INSERT into employeesdb (name,emaill,address)values\(?,?,?)",(name,emaill,address))
                con.commit()
                msg="Employee successfully Added"
       except:
            con.rollback()
            msg="We can not add the employee to the list"
       finally:
         return render_template("success25.html",msg="msg")
         con.close()
@app.route("/view")
def view():
    con=sqlite3.connect("employee.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from employeesdb")
    rows=cur.fetchall()
    return render_template("view25.html",rows=rows)
@app.route("/delete")
def delete():
    return render_template("delete25.html")
@app.route("/deleterecord",methods=['POST'])
def deleterecord():
    id=request.form["id"]
    with sqlite3.connect("employee.db") as con:
        try:
          cur=con.cursor()
          cur.execute("delete from employeesdb where id=?",id)
          msg="reccord successfully deleted"
        except:
          msg="can not be deleted"
        finally:
          return render_template("delete25.html",msg="msg")
if __name__ =="__main__":
    app.run(debug=True)
         
                
    
