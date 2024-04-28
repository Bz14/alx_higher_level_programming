#!/usr/bin/python3
""" Python script to get all states form a database """
import sys
import MySQLdb


""" Function to list all states in a database """


def list_cities(username, password, database, search):
    """ Fetch states form database """
    conn = MySQLdb.connect(host="localhost",
                           user=username,
                           password=password,
                           database=database,
                           port=3306)
    cursor = conn.cursor()
    query = ("SELECT * FROM cities INNER JOIN "
             "states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (search,))
    res = cursor.fetchall()
    name = [val[2] for val in res]
    print(", ".join(name))
    cursor.close()
    conn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    list_cities(username, password, database, search)
