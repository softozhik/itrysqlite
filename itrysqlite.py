#!/usr/bin/env python3

import sqlite3

def insert_data(data):
    try:
        cursor.execute("""insert into computers values (data);""")
        connect.commit()
    except sqlite3.Error as e:
        print (e)

connect=sqlite3.connect("mydb.sqlite")
cursor=connect.cursor()

cursor.close()