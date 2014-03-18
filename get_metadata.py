#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read car column metadata using Python.

import psycopg2
import sys


conn = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("SELECT * FROM car")
    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()

    print "%s %-10s %s" % (col_names[0], col_names[1], col_names[2])
    for row in rows:
        print "%2s %-10s %s" % row

except psycopg2.databaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
