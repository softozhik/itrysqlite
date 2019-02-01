#!/usr/bin/env python3

import sqlite3

connect=sqlite3.connect("mydb.sqlite")
cursor=connect.cursor()

# create database if not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS "computers" 
    ("User"	TEXT,
	"CompName"	TEXT NOT NULL UNIQUE,
	"OS"	TEXT NOT NULL,
	"Inventory"	INTEGER NOT NULL UNIQUE)
    """)
connect.commit()

# insert data in database
try:
    cursor.execute(
        """insert into computers values
        ("Ivan Ivanov", "WS-1", "Windows 10", 1)
        """
    )
    connect.commit()
except sqlite3.Error as e:
    print (e)


# insert more data in database
comps = [("Hachok Fedorov", "WS-2", "Windows 8", "3"),
("Pavel Fedorov", "WS-3", "Windows 7", "2"),
("Cat Koshkina", "WS-4", "Windows 10", "4")]
try:
    cursor.executemany("insert into computers values (?,?,?,?)", comps)
    connect.commit()
except sqlite3.Error as e:
    print (e)