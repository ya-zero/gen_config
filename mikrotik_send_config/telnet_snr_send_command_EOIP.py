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
          stdin, stdout, stderr = client.exec_command("/interface eoip add name=eoip_to_192.168.30.254 remote-address=192.168.30.254 tunnel-id=30"+ip)
          data=stdout.read()+stderr.read()
          print (data)
          client.close()
      except:
          print ('no auth')

for host in ipaddress.ip_network('192.168.30.0/24'):
    if subprocess.run(['ping',str(host),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
       print (host,'add command')
       ip=str(host).split('.')[-1]
       show_command = send_command(str(host),ip)
    else:
        print (host,'not ping')
