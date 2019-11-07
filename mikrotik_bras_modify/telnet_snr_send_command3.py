# -*- coding: utf-8 -*-
# iz spiska yaml
import paramiko
import yaml
import time
from pprint import pprint

# выполнение одной комманды из списка commands=[,,,,]
def send_command(dev,command):
          client=paramiko.SSHClient()
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          client.connect(hostname=dev['ip'],
                         username=dev['username'],
                         password=dev['password'],
                         look_for_keys=False,
                         allow_agent=False
                         )
          with client.invoke_shell() as ssh:
               ssh.recv(1000).decode('utf-8')
               ssh.send ('/interface  print'+'\r')
               time.sleep(5)
               output=ssh.recv(9000).decode('utf-8')
               print (output)
          client.close()
def read_device_yaml(f_device):
    with open(f_device,'r') as f:
           list_device=yaml.load(f)
    return list_device


file_device  = 'devices.yaml'
command='/interface pppoe-server server set authentication=pap,chap,mschap2 one-session-per-host=no [find where intreface=br_vl_BRAS]'
device = read_device_yaml(file_device)
show_command = send_command(device,command)
