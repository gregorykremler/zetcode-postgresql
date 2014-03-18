#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create an image table and insert a binary-encoded image file from the
# current working directory.

import psycopg2
import sys


def read_image():
    f_in = None
    try:
        f_in = open('photo.jpg', 'rb')
        img = f_in.read()
        return img
    except IOError, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if f_in:
            f_in.close()

conn = None
try:
    conn = psycopg2.connect(database='testdb', user='gregorykremler')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE image (
                       id INT PRIMARY KEY,
                       data BYTEA
                )""")
    data = read_image()
    binary = psycopg2.Binary(data)
    cur.execute("INSERT INTO image (id, data) VALUES (0, %s)", (binary,))

    conn.commit()

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
