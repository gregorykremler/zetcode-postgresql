#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read query results row-by-row with .fetchone().

import psycopg2
import sys


conn = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("SELECT * FROM car")

    while True:
        row = cur.fetchone()
        if row is None:
            break
        print row[0], row[1], row[2]

except psycopg2.DatabaseError as e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
