#!/usr/bin/python3
"""
get all states
"""
from sys import argv
import MySQLdb

db = MySQLdb.connect(host='localhost:3306',
                     user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
print(rows)