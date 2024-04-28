#!/usr/bin/python3
import MySQLdb
import sys
""" Python script to get all states form a database """


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           password=sys.argv[2],
                           database=sys.argv[3],
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    res = cursor.fetchall()
    for val in res:
        print(f"({val[0]}, '{val[1]}')")
