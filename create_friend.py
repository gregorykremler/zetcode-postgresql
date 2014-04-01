#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create a friend table and insert rows in autocommit mode.

import psycopg2
import sys


conn = None
try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("""CREATE TABLE friend (
                       id serial PRIMARY KEY,
                       name VARCHAR(10)
                )""")
    cur.execute("INSERT INTO friend (name) VALUES ('Jane')")
    cur.execute("INSERT INTO friend (name) VALUES ('Tom')")
    cur.execute("INSERT INTO friend (name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO friend (name) VALUES ('Jim')")
    cur.execute("INSERT INTO friend (name) VALUES ('Robert')")
    cur.execute("INSERT INTO friend (name) VALUES ('Patrick')")

except psycopg2.DatabaseError as e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
