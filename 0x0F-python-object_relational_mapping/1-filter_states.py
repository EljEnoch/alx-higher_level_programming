#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":

    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")

    rows = cur.fetchall()

    for eachrow in rows:
        print(eachrow)

    cur.close()
    con.close()
