#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Export car data to a new file in the current working directory.

import psycopg2
import sys


conn = None
f_out = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    f_out = open('car.txt', 'w')
    cur.copy_to(f_out, 'car', sep='|')

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

except IOError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
    if f_out:
        f_out.close()
