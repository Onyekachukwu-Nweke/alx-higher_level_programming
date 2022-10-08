#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
Usage: ./4-cities_by_state.py <mysql username> \
                                <mysql password> \
                                <database name>
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                    FROM `cities` AS `c` \
                    INNER JOIN `states` AS `s` \
                    ON `c`.`state_id` = `s`.`id` \
                    ORDER BY `c`.`id` ASC")

    [print(city) for city in cur.fetchall()]

    cur.close()
    db.close()
