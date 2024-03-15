#!/usr/bin/python3
"""
filter cities
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states\
                INNER JOIN cities ON cities.state_id = states.id\
                WHERE states.name='%s'\
                ORDER BY cities.id", argv[4])
    rows = cur.fetchall()
    for row in rows:
        print(row)
