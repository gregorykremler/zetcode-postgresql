#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create a car table and insert rows with SQL.

import psycopg2
import sys


conn = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE car (
                       id INT PRIMARY KEY,
                       name VARCHAR(20),
                       price INT
                )""")
    cur.execute("""INSERT INTO car (id, name, price)
                       VALUES (1, 'Audi', 52642)""")
    cur.execute("""INSERT INTO car (id, name, price)
                       VALUES (2, 'Mercedes', 57127)""")
    cur.execute("""INSERT INTO car (id, name, price)
                       VALUES (3, 'Skoda', 9000)""")
    cur.execute("""INSERT INTO car (id, name, price)
                       VALUES (4, 'Volvo', 29000)""")
    cur.execute("""INSERT INTO car (id, name, price)
                       VALUES (5, 'Bentley', 350000)""")
    cur.execute("""INSERT INTO car (id, name, price)
                       VALUES (6, 'Citroen', 21000)""")
    cur.execute("""INSERT INTO car (id, name, price)
                       VALUES (7, 'Hummer', 41400)""")
    cur.execute("""INSERT INTO car (id, name, price)
                       VALUES (8, 'Volkswagen', 21600)""")

    conn.commit()

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
