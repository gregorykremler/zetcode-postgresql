#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import data from a file in the current working directory to the car
# table.

import psycopg2
import sys


conn = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("DELETE FROM car")

    try:
        with open('car.txt', 'r') as f_in:
            cur.copy_from(f_in, 'car', sep='|')
    except IOError as e:
        if conn:
            conn.rollback()
        print 'Error %d: %s' % (e.errno, e.strerror)
        sys.exit(1)

    conn.commit()

except psycopg2.DatabaseError as e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
