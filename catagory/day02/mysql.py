#!/usr/bin/python
# -*- coding:utf-8 -*-

# @Time :2019-11-06 16:24
# @Author: cd
# @FileName:mysql.py
# @Copyright: @2019-2020
import MySQLdb
db = MySQLdb.connect(host='localhost', user='root', passwd='ana1215', db='october', port=3306)

cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()

print 'Database version :%s' % data
db.close()
