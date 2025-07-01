import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import argparse

import os
import numpy as np
import os

import pandas as pd

 
 
 

def db_connect(): 
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="news")
    c = _conn.cursor()

    return c, _conn

# -------------------------------register-----------------------------------------------------------------
def user_reg(username,email,password,add,ph):
    try:
        status=user_loginact(username, password)
        if status==1:
            return 0
        c, conn = db_connect()
        print(username, password, email)
        j = c.execute("INSERT INTO buser(username, email, password, ph,location) VALUES (%s, %s, %s, %s, %s)", 
               (username, email, password, ph, add))
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
     
# -------------------------------------Login --------------------------------------
def user_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from buser where username='" +
                      username+"' and password='"+password+"'")
        data = c.fetchall()
        print(data)     
       
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))
    

# -------------------------------register-----------------------------------------------------------------
def auser_reg(username,email,password):
    try:
        status=auser_loginact(username, password)
        if status==1:
            return 0
        c, conn = db_connect()
        print(username, password, email)
        j = c.execute("INSERT INTO auser(username, email, password) VALUES (%s, %s, %s)", 
               (username, email, password))
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
     
# -------------------------------------Login --------------------------------------
def auser_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from auser where username='" +
                      username+"' and password='"+password+"'")
        data = c.fetchall()
        print(data)     
       
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))
    
def addnewsr(u, t, n, s, hash2):
    try:
        c, conn = db_connect()  # Ensure `db_connect()` uses UTF-8 encoding
        # Print statements to check values
        print(u, t, n, s)
        
        # Insert data into the database
        j = c.execute("INSERT INTO newst(u, t, n, s, h) VALUES (%s, %s, %s, %s, %s)", 
                      (u, t, n, s, hash2))
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return str(e)

def view1(username):
    try:
        c, conn = db_connect()
        query = "SELECT * FROM newst WHERE u=%s"
        c.execute(query, (username,))
        result = c.fetchall()
        conn.commit()
        conn.close()
        print(result)
        return result 
    except Exception as e:
        return str(e)
def view():
    try:
        c, conn = db_connect()
        query = "SELECT * FROM newst"
        c.execute(query)
        result = c.fetchall()
        conn.commit()
        conn.close()
        print(result)
        return result 
    except Exception as e:
        return str(e)
def view3(username):
    try:
        c, conn = db_connect()
        query = "SELECT * FROM newssend WHERE r=%s"
        c.execute(query, (username,))
        result = c.fetchall()
        conn.commit()
        conn.close()
        print(result)
        return result 
    except Exception as e:
        return str(e)

def s(s1,param1,param2,param3,se,r):
    try:
        c, conn = db_connect()
        # Insert data into the database
        j = c.execute("INSERT INTO newssend(newsid, t, n, s, r,u) VALUES (%s, %s, %s, %s, %s,%s)", 
                      (param1,param2,param3,se,r,s1))
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return str(e)
def report(param1):
    try:
        c, conn = db_connect()
        query = "SELECT * FROM newssend WHERE newsid=%s"
        c.execute(query, (param1,))
        result = c.fetchall()
        conn.commit()
        conn.close()
        print(result)
        return result 
    except Exception as e:
        return str(e)
if __name__ == "__main__":
    print(db_connect())
