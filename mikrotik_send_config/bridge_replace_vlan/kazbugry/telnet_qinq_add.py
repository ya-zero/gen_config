# -*- coding: utf-8 -*-
# iz spiska yaml
import MySQLdb
import paramiko
import yaml
import time
import sys
import ipaddress
import subprocess
from pprint import pprint

# выполнение одной комманды из списка commands=[,,,,]
def sql_connect():
    try:
      sql_connect = MySQLdb.connect(host='192.168.0.5',
                              user='script',
                              password='script',
                              charset='utf8',
                              use_unicode=False,
                              db='radio')

      cursor=sql_connect.cursor()
      return cursor
    except MySQLdb.Error as error:
      return error


def send_command(host,vlan_id):
      try:
          client=paramiko.SSHClient()
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          client.connect(hostname=host,
                         username='root',
                         password='1abrakadabra2',
                         look_for_keys=False,
                         allow_agent=False)
          stdin, stdout, stderr = client.exec_command("/interface vlan add vlan-id={0} interface=ether1.4000 name=ether1.4000.{0} comment=qinq_pppoe".format(vlan_id))
          time.sleep(1)
          data=stdout.read()+stderr.read()
          print (data)
          client.close()
      except:
          print ('no auth')

cursor=sql_connect()
print ('dd',cursor)



sector_replace=['192.168.30.51','192.168.30.116','192.168.30.53','192.168.30.54','192.168.30.81','192.168.30.82','192.168.30.90','192.168.30.10','192.168.30.100','192.168.30.80','192.168.30.83']
sector_ignore_def=['192.168.30.0','192.168.30.1','192.168.30.254']
for host in ipaddress.ip_network('192.168.30.0/24'):
   if str(host) in sector_replace:
     print ('host',str (host))
     if subprocess.run(['ping',str(host),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
       print (host,'add command')
       if cursor:
           request='''SELECT DB.base FROM devices_ip_addresses DIP LEFT JOIN devices_bases DB ON DB.ip_id = DIP.id WHERE DIP.ip ="%s";''' % str(host)
           try:
              cursor.execute(request)
              for row1 in cursor:
               vlan_id=str(row1[0])[2:5]
           except MySQLdb.Error as error:
              print ('MySQL SELECT error {}'.format(error))
           print ("add vlan-id={0} interface=ether1.4000 name=ether1.4000.{0} comment=qinq".format(vlan_id))
           show_command = send_command(str(host),vlan_id)
     else:
        print (host,'not ping')
