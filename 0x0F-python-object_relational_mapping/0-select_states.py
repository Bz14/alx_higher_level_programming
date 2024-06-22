#!/usr/bin/python3
""" Sql query to list all states."""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db =  MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    curr = db.cursor()
    curr.execute("SELECT * FROM states ORDER BY id ASC")
    rows = curr.fetchall()
    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))
    curr.close()
    db.close()
