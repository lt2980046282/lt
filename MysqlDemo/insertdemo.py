#!/usr/bin/python
# -*- coding: gbk -*-

import MySQLdb

# �����ݿ�����
db = MySQLdb.connect("localhost", "root", "lt980727", "manhua", charset='utf8' )

# ʹ��cursor()������ȡ�����α�
cursor = db.cursor()

# SQL �������
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # ִ��sql���
   cursor.execute(sql)
   # �ύ�����ݿ�ִ��
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# �ر����ݿ�����
db.close()
#��������Ҳ����д��������ʽ��

