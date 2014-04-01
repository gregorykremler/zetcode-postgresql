#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read an image row and use it to create a new image file in the current
# working directory.

import psycopg2
import sys


def write_image(data):
    try:
        with open('photo2.jpg', 'wb') as f_out:
            f_out.write(data)
    except IOError as e:
        print 'Error %d: %s' % (e.errno, e.strerror)
        sys.exit(1)

conn = None
try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("SELECT data FROM image LIMIT 1")
    data = cur.fetchone()[0]
    write_image(data)

except psycopg2.DatabaseError as e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
