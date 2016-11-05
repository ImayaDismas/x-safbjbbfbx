#!\usr\bin\python3
# -*- coding: utf-8 -*-



import MySQLdb
import sys
from PIL import Image
import PIL.Image

conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="target")
image = Image.open('web.png')

blob_value = Image.open('web.png', 'r').read()

cur = conn.cursor()
cur.execute("insert into testblob set image='%s'" % MySQLdb.escape_string(blob_value))
# sql1='select * from image'
# conn.commit()
# cur.execute(sql1)
# data=cur.fetchall()
# print ( type(data[0][0]) )
# file_like=io.StringIO(data[0][0])
# img=PIL.Image.open(file_like)
# img.show()

conn.close()
