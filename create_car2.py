#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create a car table and insert rows with Python.

import psycopg2
import sys


car = ((1, 'Audi', 52642),
       (2, 'Mercedes', 57127),
       (3, 'Skoda', 9000),
       (4, 'Volvo', 29000),
       (5, 'Bentley', 350000),
       (6, 'Citroen', 21000),
       (7, 'Hummer', 41400),
       (8, 'Volkswagen', 21600))

conn = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS car")
    cur.execute("""CREATE TABLE car (
                       id INT PRIMARY KEY,
                       name VARCHAR(20),
                       price INT
                )""")
    query = "INSERT INTO car (id, name, price) VALUES (%s, %s, %s)"
    cur.executemany(query, car)

    conn.commit()

except psycopg2.DatabaseError as e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
