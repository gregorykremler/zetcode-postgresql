#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read a car row with a paramaterized query.

import psycopg2
import sys


conn = None

uId = 3

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("SELECT * FROM car WHERE id=%(id)s", {'id': uId})
    print cur.fetchone()

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
