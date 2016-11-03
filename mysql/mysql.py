#!/usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="test")
cur = conn.cursor()

cur.execute("SELECT * FROM test_data")
row = cur.fetchone()
while row is not None:
    print (row[0],row[1],row[2])
    row = cur.fetchone()

cur.close()
conn.close()
sys.exit(1)
