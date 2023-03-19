#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":

    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    with con.cursor() as cur:
        cur.execute("""
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id=states.id
            WHERE BINARY states.name = %s
            ORDER BY cities.id
    """, (argv[4], ))
        rows = cur.fetchall()

        mysep = ""
        for eachrow in rows:
            print(mysep + str(*eachrow), end="")
            mysep = ", "

    print()
