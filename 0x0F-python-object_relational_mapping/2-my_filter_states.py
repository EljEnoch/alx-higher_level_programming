#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":

    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    cur = con.cursor()

    sql = "SELECT * FROM states WHERE BINARY name = '{}'".format(argv[4])
    cur.execute(sql + " ORDER BY id")

    rows = cur.fetchall()

    for eachrow in rows:
        print(eachrow)

    cur.close()
    con.close()
