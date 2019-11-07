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
def send_command(host,command):
      try:
          client=paramiko.SSHClient()
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          client.connect(hostname=host,
                         username='root',
                         password='1abrakadabra2',
                         look_for_keys=False,
                         allow_agent=False)

          stdin, stdout, stderr = client.exec_command("/interface pppoe-server server print")
#          stdin, stdout, stderr = client.exec_command("/interface pppoe-server server set authentication=pap,chap,mschap2 one-session-per-host=yes [find where interface =br_vl_BRAS]")
          data=stdout.read()+stderr.read()
          client.close()
          print (data)
      except:
          print ('no auth')
command="/interfaces pppoe-server server set authentication=pap,chap,mschap2 one-sessions-per-host=yes [find where intreface=br_vl_BRAS]"
for host in ipaddress.ip_network('192.168.30.0/24'):
    if subprocess.run(['ping',str(host),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
       print (host,'add command')
       show_command = send_command(str(host),command)
    else:
        print (host,'not ping')
