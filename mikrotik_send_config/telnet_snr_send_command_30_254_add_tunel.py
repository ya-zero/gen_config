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
                         username='admin',
                         password='',
                         look_for_keys=False,
                         allow_agent=False)
          num=2
          while num < 126:
            if subprocess.run(['ping','192.168.30.'+str(num),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
               #/interface list member add list=eoip interface=eoip_to_192.168.30."+str(num)"
               stdin, stdout, stderr = client.exec_command("/interface list member add list=eoip interface=eoip_to_192.168.30."+str(num))
               data=stdout.read()+stderr.read()
               print (data)
#                print ("/interface eoip add name=eoip_to_192.168.30."+str(num)+" remote-address=192.168.30."+str(num)+" tunnel-id=30"+str(num))
               print ('ping to '+str(num))
            num += 1
          client.close()
      except:
          print ('no auth')

for host in ipaddress.ip_network('192.168.30.254/32'):
    if subprocess.run(['ping',str(host),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
       print (host,'add command')
       ip=str(host).split('.')[-1]
       show_command = send_command(str(host),ip)
    else:
        print (host,'not ping')
