#!/usr/bin/python
# -*- coding: gbk -*-
from mysql.connector import connect


class YingHua:
    conn = connect(host='localhost', user="root", passwd="lt980727")
    dbs = conn.cursor()
    dbs.execute('show databases')
    for db in dbs:
        print(db)

YingHua()