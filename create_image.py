#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create an image table and insert a binary-encoded image file from the
# current working directory.

import psycopg2
import sys


def read_image():
    try:
        with open('photo.jpg', 'rb') as f_in:
            img = f_in.read()
            return img
    except IOError as e:
        print 'Error %d: %s' % (e.errno, e.strerror)
        sys.exit(1)

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

except psycopg2.DatabaseError as e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
