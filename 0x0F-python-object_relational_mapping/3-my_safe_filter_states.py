#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":

    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    with con.cursor() as cur:
        cur.execute("""
            SELECT *
            FROM states
            WHERE BINARY name = %s
            ORDER BY id
    """, (argv[4], ))

        rows = cur.fetchall()

        for eachrow in rows:
            print(eachrow)
