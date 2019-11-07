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

# выполнение одной комманды из списка commands=[,,,,]
def send_command(host):
      try:
          with netmiko.ConnectHandler(device_type="cisco_ios",username="root",password="1abrakadabra2",verbose=True,ip=host,default_enter="\n\r"):
             result_1=ssh.send_command("/interface vlan")
             result_2=ssh.send_command("add vlan-id=4005 interface=ether1 name=ether1.4005 comment=q4005")
             print (result_1,result_2)
      except:
          print ('no auth')

sector_replace=['192.168.30.129','192.168.30.3','192.168.30.36','192.168.30.133','192.168.30.43','192.168.30.77','192.168.30.88','192.168.30.89','192.168.30.104']
sector_ignore_def=['192.168.30.0','192.168.30.1','192.168.30.254']
for host in ipaddress.ip_network('192.168.30.0/24'):
   if str(host) in sector_replace:
     print ('host',str (host))
     if subprocess.run(['ping',str(host),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
       print (host,'add command')
       show_command = send_command(str(host))
     else:
        print (host,'not ping')
