#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Print the PostgreSQL database version.

import psycopg2
import sys


conn = None

try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()
    cur.execute("SELECT version()")
    version = cur.fetchone()
    print version

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
