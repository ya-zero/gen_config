# -*- coding: utf-8 -*-
import yaml
from pprint import pprint
# открытие файла
def read_device_yaml(f_device):
    with open(f_device,'r') as f:
           list_device=yaml.load(f)
    return list_device

file_device  = 'host.yml'
try:
  devices = read_device_yaml(file_device)
  pprint  (devices)
except: print ('not open file device list')

#pprint (devices)