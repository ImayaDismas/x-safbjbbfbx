#!\usr\bin\python3
# -*- coding: utf-8 -*-



import MySQLdb
import sys
from PIL import Image
import PIL.Image

def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo

def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def update_blob(filename):
    # read file
    data = read_file(filename)

    # print(data)

    # prepare update query and data
    query = "INSERT INTO testblob " \
            "SET image = %s "

    args = (data, )

    try:
        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="target")
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def read_blob(author_id, filename):
    # select photo column of a specific author
    query = "SELECT image FROM testblob"

    try:
        # query blob data form the authors table
        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="target")
        cursor = conn.cursor()
        cursor.execute(query,)
        photo = cursor.fetchone()[0]

        # write blob data into a file
        write_file(photo, filename)

    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def main():
    # update_blob("web.png")
    read_blob(9,"/home/imaya/Documents/Projects/x-safbjbbfbx/mysql/images/web.png")

if __name__ == '__main__':
    main()
