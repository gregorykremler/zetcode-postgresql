#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use a dict cursor to reference the data by column name.

import psycopg2
import psycopg2.extras
import sys


conn = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute("SELECT * FROM car")
    rows = cur.fetchall()

    for row in rows:
        print "%s %s %s" % (row['id'], row['name'], row['price'])

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
