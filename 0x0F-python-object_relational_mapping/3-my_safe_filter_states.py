#!/usr/bin/python3
"""
my filter states
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states
             WHERE BINARY name=%s
             ORDER BY id ASC"
    cur.execute(query, argv[4])
    rows = cur.fetchall()
    for row in rows:
        print(row)
