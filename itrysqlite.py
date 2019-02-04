#!/usr/bin/env python3

import sqlite3

def insert_Inventory(inv):
    cursor=connect.cursor()
    comp=(inv, None, None, None)
    try:
        cursor.execute("""insert into computers values (?, ?, ?, ?)""", comp)
        connect.commit()
    except sqlite3.Error as e:
        print (e)
    cursor.close()

def update_User(inv, user):
    cursor=connect.cursor()
    try:
        cursor.execute("""update computers set User = ? where Inventory = ?""", (user, inv))
        connect.commit()
    except sqlite3.Error as e:
        print (e)
    cursor.close()

def update_OS(inv, os):
    cursor=connect.cursor()
    try:
        cursor.execute("""update computers set OS = ? where Inventory = ?""", (os, inv))
        connect.commit()
    except sqlite3.Error as e:
        print (e)
    cursor.close()

def update_CompName(inv, compname):
    cursor=connect.cursor()
    try:
        cursor.execute("""update computers set CompName = ? where Inventory = ?""", (compname, inv))
        connect.commit()
    except sqlite3.Error as e:
        print (e)
    cursor.close()

connect=sqlite3.connect("mydb.sqlite")

#comp=(inv, user, os, compname)

inv = input("Inventory (числовой, уникальный): ")
insert_Inventory(inv)
user= input("User: ")
update_User(inv,user)
os = input("OS: ")
update_OS(inv, os)
compname = input("CompName: ")
update_CompName(inv, compname)