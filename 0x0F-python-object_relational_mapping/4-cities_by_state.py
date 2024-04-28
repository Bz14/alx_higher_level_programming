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
    query = ("SELECT c.id, c.name, s.name "
             "FROM cities as c INNER JOIN states as s ON "
             "c.state_id = s.id ORDER BY c.id ASC")
    cursor.execute(query)
    res = cursor.fetchall()
    for val in res:
        print(val)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
