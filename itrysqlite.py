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


connect=sqlite3.connect("mydb.sqlite")


inv = input("Inventory (числовой, уникальный): ")
#user= input("User: ")
#os = input("OS: ")
#compname = input("CompName: ")
#comp=(inv, user, os, compname)
#print(comp)
insert_Inventory(inv)

