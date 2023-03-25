#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC".format(argv[4]))

    for state in cursor.fetchall():
        if state[1] == argv[4]:
            print(state)

    cursor.close()
    db.close()
