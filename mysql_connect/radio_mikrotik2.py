# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect (host="192.168.0.5",user='root',password='yfbvtyjdfybt',db='radio',charset='utf8')
cursor = conn.cursor()
sql = ("SELECT DIP.ip FROM devices_bases DB LEFT JOIN devices_ip_addresses DIP ON DB.ip_id = DIP.id WHERE DB.is_deleted = 0")
cursor.execute(sql)
#print (cursor)
data = cursor.fetchall()
for i in data:
     print (i)
