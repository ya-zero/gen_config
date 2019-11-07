# -*- coding: utf-8 -*-
# iz spiska yaml
import paramiko
import yaml
import time
import sys
import ipaddress
import subprocess
import netmiko
from pprint import pprint
import logging

# выполнение одной комманды из списка commands=[,,,,]
def send_command(host):
      try:
          client=paramiko.SSHClient()
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          client.connect(hostname=host,
                         username='root',
                         password='1abrakadabra2',
                         look_for_keys=False,
                         allow_agent=False)
          stdin, stdout, stderr = client.exec_command("/interface vlan add vlan-id=4005 interface=ether1 name=ether1.4005 comment=q4005")
          data=stdout.read()+stderr.read()
          print (data)
          client.close()
      except:
          print ('no auth')

logging.basicConfig(filename='test.log',level=logging.DEBUG)
sector_replace=['192.168.30.129','192.168.30.3','192.168.30.36','192.168.30.133','192.168.30.43','192.168.30.77','192.168.30.88','192.168.30.89','192.168.30.104']
sector_ignore_def=['192.168.30.0','192.168.30.1','192.168.30.254']
for host in ipaddress.ip_network('192.168.30.0/24'):
   if str(host) in sector_replace:
     print ('host1:',str (host))
     if subprocess.run(['ping',str(host),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
       print (host,'add command')
       ip=str(host).split('.')[-1]
       show_command = send_command(str(host))
       print ("host2:",host,ip)
     else:
        print (host,'not ping')
