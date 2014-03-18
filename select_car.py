#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read query results altogether with .fetchall().

import psycopg2
import sys


conn = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("SELECT * FROM car")
    rows = cur.fetchall()
    for row in rows:
        print row

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
