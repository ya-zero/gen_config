# -*- coding: utf-8 -*-
# выполнение комманд из file_config
# на устройствах из devices.yaml
import netmiko
import yaml
from pprint import pprint

# выполнение комманд
def send_show_command(device,commands):
     try:
       with netmiko.ConnectHandler(**device,verbose=True) as ssh:
            result=ssh.send_config_set(commands)
            print('commands:',result)
     except:
           print('error')
     if result:
        return {device['ip']:result}

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
file_config  = '192.168.0.227.cfg'
command=read_config(file_config).strip().split('\n')
devices = read_device_yaml(file_device)
for dev in  devices['switch']:
     show_command=send_show_command(dev,command)
     pprint(show_command)