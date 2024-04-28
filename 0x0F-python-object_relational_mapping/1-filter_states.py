#!/usr/bin/python3
""" Python script to get all states form a database """
import sys
import MySQLdb


""" Function to list all states in a database """


def list_states(username, password, database):
    """ Fetch states form database """
    conn = MySQLdb.connect(host="localhost",
                           user=username,
                           password=password,
                           database=database,
                           port=3306)
    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE "
    query += "'N%' ORDER BY states.id ASC"
    cursor.execute(query)
    res = cursor.fetchall()
    for val in res:
        print(f"({val[0]}, '{val[1]}')")
    cursor.close()
    conn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
