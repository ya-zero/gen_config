# -*- coding: utf-8 -*-
# iz spiska yaml
import paramiko
import yaml
import time
import sys
import ipaddress
import subprocess
from pprint import pprint

# выполнение одной комманды из списка commands=[,,,,]
def send_command(host,ip):
      try:
          client=paramiko.SSHClient()
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          client.connect(hostname=host,
                         username='root',
                         password='1abrakadabra2',
                         look_for_keys=False,
                         allow_agent=False)
          stdin, stdout, stderr = client.exec_command("/interface vlan add vlan-id=4001 interface=ether1 name=ether1.4001 comment=qinq")
          data=stdout.read()+stderr.read()
          print (data)
          client.close()
      except:
          print ('no auth')

sector_ignore=['192.168.30.33','192.168.30.66','192.168.30.8','192.168.30.38','192.168.30.39','192.168.30.40','192.168.30.156','192.168.30.157','192.168.30.158']
sector_ignore_def=['192.168.30.0','192.168.30.1','192.168.30.254']
for host in ipaddress.ip_network('192.168.30.0/24'):
   if str(host) in sector_ignore:
     print ('host',str (host))
     if subprocess.run(['ping',str(host),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
       print (host,'add command')
       ip=str(host).split('.')[-1]
       show_command = send_command(str(host),ip)
     else:
        print (host,'not ping')
