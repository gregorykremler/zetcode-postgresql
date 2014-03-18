#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read table name metadata using SQL.

import psycopg2
import sys

conn = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("""SELECT table_name FROM information_schema.tables
                       WHERE table_schema = 'public'""")
    rows = cur.fetchall()

    for row in rows:
        print row[0]

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
