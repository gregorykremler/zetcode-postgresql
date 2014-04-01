#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Export car data to a new file in the current working directory.

import psycopg2
import sys


conn = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    try:
        with open('car.txt', 'w') as f_out:
            cur.copy_to(f_out, 'car', sep='|')
    except IOError as e:
        print 'Error %d: %s' % (e.errno, e.strerror)
        sys.exit(1)

except psycopg2.DatabaseError as e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
