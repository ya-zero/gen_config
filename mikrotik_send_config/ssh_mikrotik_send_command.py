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
host='192.168.0.9'
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host,
                         username='admin',
                         password='',
                         look_for_keys=False,
                         allow_agent=False)

for ip_loopback in ipaddress.ip_network('195.178.22.0/25'):
   command="""/ip address add address={0} interface=loopback network={0} """.format(ip_loopback)
   stdin, stdout, stderr = client.exec_command(command)
   data=stdout.read()+stderr.read()
   print (data)
client.close()


