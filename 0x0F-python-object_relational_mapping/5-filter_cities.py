#!/usr/bin/python3
"""
Displays all cities of a given state from the
states table of the database hbtn_0e_4_usa.
Safe from SQL injections.
Usage: ./5-filter_cities.py <mysql username> \
                            <mysql password> \
                            <database name> \
                            <state name searched>
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], port=3306,
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT `cities`.`name` FROM cities \
                INNER JOIN `states` ON \
                `cities`.`state_id` = `states`.`id` \
                WHERE `states`.`name` = %s \
                ORDER BY `cities`.`id` ASC", (argv[4], ))

    print(", ".join([city[0] for city in cur.fetchall()]))
