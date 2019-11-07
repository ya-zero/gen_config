# -*- coding: utf-8 -*-
# iz spiska yaml
import netmiko
import yaml
from pprint import pprint

# выполнение одной комманды из списка commands=[,,,,]
def send_show_command(dev,commands):
    with  netmiko.ConnectHandler(**dev,verbose=True) as ssh:
          result=ssh.send_config_set(commands)
    return {dev['ip']:result}


def read_device_yaml(f_device):
    with open(f_device,'r') as f:
           list_device=yaml.load(f)
    return list_device

def read_config(f_config):
    with open(f_config,'r') as f:
           config=f.read()
    return config

#command = 'sh version'
file_device  = 'devices.yaml'
#file_config  = '192.168.0.227.cfg'
#commands=read_config(file_config).strip().split('\n')
commands=['logging 192.168.0.20']
devices = read_device_yaml(file_device)
for dev in  devices['switch']:
   for command in commands:
     show_command=send_show_command(dev,command)
     print(show_command)