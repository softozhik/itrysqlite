#!/usr/bin/env python3

import sqlite3

connect=sqlite3.connect("mydb.sqlite")
cursor=connect.cursor()



connect.commit()
