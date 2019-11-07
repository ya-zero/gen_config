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
def send_command(host):
      try:
          client=paramiko.SSHClient()
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          client.connect(hostname=host,
                         username='root',
                         password='1abrakadabra2',
                         look_for_keys=False,
                         allow_agent=False)
          command="""/ip firewall filter set [find action=drop] disabled=yes;
          /ip firewall filter remove [find chain=forward ];
          /ip firewall filter remove [find chain=input ];
          /ip firewall filter remove [find chain=our_addr ];
          /ip firewall filter add action=drop chain=input comment="Drop invalid connection packets" connection-state=invalid  disabled=yes;
          /ip firewall filter add action=accept chain=input comment="Allow established and related state connection" connection-state=established,related;
          /ip firewall filter add action=accept chain=input protocol=icmp;
          /ip firewall filter add action=accept chain=input protocol=gre;
          /ip firewall filter add action=accept chain=input protocol=ospf;
          /ip firewall filter add action=jump chain=input connection-state=new jump-target=our_addr;
          /ip firewall filter add action=drop chain=input comment="All other input-packets are DROPED"  disabled=yes;
          /ip firewall filter add action=accept chain=our_addr in-interface=ether1.30 src-address=192.168.0.0/24;
          /ip firewall filter set [find action=drop] disabled=no;"""

#          stdin, stdout, stderr = client.exec_command("/ip firewall filter enable    [find where chain=forward]")
          stdin, stdout, stderr = client.exec_command(command)
          data=stdout.read()+stderr.read()
          print (data)
          client.close()
      except:
          print ('no auth')
for host in ipaddress.ip_network('192.168.30.0/24'):
    if subprocess.run(['ping',str(host),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
       print (host,'add command')
       show_command = send_command(str(host))
    else:
        print (host,'not ping')


