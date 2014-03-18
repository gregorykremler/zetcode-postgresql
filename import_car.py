#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import data from a file in the current working directory to the car
# table.

import psycopg2
import sys


conn = None
f_in = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("DELETE FROM car")
    f_in = open('car.txt', 'r')
    cur.copy_from(f_in, 'car', sep='|')

    conn.commit()

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    sys.exit(1)

except IOError, e:
    if conn:
        conn.rollback()
    print 'Error %d: %s' % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    if conn:
        conn.close()
    if f_in:
        f_in.close()
