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
#          stdin, stdout, stderr = client.exec_command("/interface eoip add name=eoip_to_192.168.30.254 remote-address=192.168.30.254 tunnel-id=30"+ip)
#          stdin, stdout, stderr = client.exec_command("/interface bridge filter set numbers=[find chain=forward action=drop] disabled=yes")
          stdin, stdout, stderr = client.exec_command("/interface bridge filter add action=drop chain=forward in-bridge=br_vl_PPPoE ip-protocol=udp mac-protocol=ip src-port=5678")
          stdin, stdout, stderr = client.exec_command("/interface bridge filter add action=drop chain=forward dst-port=5678 in-bridge=br_vl_PPPoE ip-protocol=udp mac-protocol=ip")
#          stdin, stdout, stderr = client.exec_command("add action=drop chain=forward in-bridge=br_vl29 ip-protocol=udp mac-protocol=ip src-port=5678")
#          stdin, stdout, stderr = client.exec_command("add action=drop chain=forward dst-port=5678 in-bridge=br_vl29 ip-protocol=udp mac-protocol=ip")

          data=stdout.read()+stderr.read()
          print (data)
          client.close()
      except:
          print ('no auth')

for host in ipaddress.ip_network('192.168.30.64/26'):
    if subprocess.run(['ping',str(host),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
       print (host,'add command')
       ip=str(host).split('.')[-1]
       show_command = send_command(str(host),ip)
    else:
        print (host,'not ping')
