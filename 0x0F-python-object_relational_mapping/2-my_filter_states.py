#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Usage: ./2-my_filter_states.py <mysql username> \
                                <mysql password> \
                                <database name> \
                                <state name searched>
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], port=3306, host="localhost",
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))

    [print(state) for state in cur.fetchall() if state[1] == argv[4]]

    cur.close()
    db.close()
