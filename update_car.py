#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Update a car row with a paramaterized query.

import psycopg2
import sys


conn = None

uId = 1
uPrice = 62300

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("UPDATE car SET price=%s WHERE id=%s", (uPrice, uId))

    conn.commit()

    print "Number of rows updated: %d" % cur.rowcount

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
