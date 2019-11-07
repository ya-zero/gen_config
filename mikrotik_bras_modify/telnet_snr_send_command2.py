# -*- coding: utf-8 -*-
# iz spiska yaml
import netmiko
import yaml
from pprint import pprint

# выполнение одной комманды из списка commands=[,,,,]
def send_command(dev,command):
    with  netmiko.ConnectHandler(**dev,verbose=True) as ssh:
          result=ssh.send_command(command)
    return {dev['ip']:result}

def read_device_yaml(f_device):
    with open(f_device,'r') as f:
           list_device=yaml.load(f)
    return list_device


file_device  = 'devices.yaml'
command='/interface pppoe-server server set authentication=pap,chap,mschap2 one-session-per-host=yes [find where intreface=br_vl_BRAS]'
device = read_device_yaml(file_device)
show_command = send_command(device,command)
print(show_command)