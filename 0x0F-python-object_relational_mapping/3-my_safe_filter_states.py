#!/usr/bin/python3
""" Sql query to list all states."""
import MySQLdb
import sys


if __name__ == "__main__":
    db =  MySQLdb.connect(host="localhost", user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], port=3306)
    search = sys.argv[4]
    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name LIKE %s", (search, ))
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    db.close()
