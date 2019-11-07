# -*- coding: utf-8 -*-
# iz spiska yaml
#переимеование интерфейсов в бридже с етш.ххх в етш1.ххх
# так как разная длинна в списке интерфейсов (когда  выкключен)  то работает два условия.

import json
import netmiko
import yaml
import logging
import time
import ipaddress
import subprocess
import re
from pprint import pprint

# выполнение одной комманды из списка commands=[,,,,]
def send_show_command(dev,commands):
  try:
    with  netmiko.ConnectHandler(**dev,default_enter="\n\r") as ssh:
          result=ssh.send_command(commands)
    return [dev['ip'],result]
  except:
    return ['no auth','0']


#logging.basicConfig(filename='test.log',level=logging.DEBUG)
#command = '/interface bridge port print where bridge=br_vl_PPPoE'
#command = '/interface bridge port print'
#number=[find bridge=br_vl_PPPOE interface~"ether\\."'
#file_device  = 'devices.yaml'
#show_command=send_show_command({'device_type':'cisco_ios','username':'root+ct80h','password':'1abrakadabra2','verbose':True,'ip':'192.168.30.20'},command)
#sector={}
#for host in ipaddress.ip_network('192.168.30.0/24'):
#     if subprocess.run(['ping',str(host),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
#          show_command=send_show_command({'device_type':'cisco_ios','username':'root+ct80h100w','password':'1abrakadabra2','verbose':True,'ip':str(host)},command)
#          br_if=[]
#          for row in show_command[1].split("\n"):
#              if len(row)>1:
#               if 'Flags' not in row and 'INTERFACE' not in row:
#                 br_if.append(re.split(' +',row.strip()))
#          if len(br_if)>1:
#             sector[str(host)]=br_if

with open('result_pred.sw','r') as f:
     sector=json.load(f)
#print (sector)
intreface_name=[]
for row in sector.keys():
      for bridg in sector[row]:
#       if len(bridg)==8:
#        if 'br_vl_PPPoE' in bridg[2] and 'ether' in bridg[1]:
#            interface_name=bridg[1].split('.')
#            pprint (interface_name)
#            if interface_name[0]=='ether':
#             command = '/interface vlan set name=ether1.{} numbers=[find name ~"{}"]'.format(interface_name[1],bridg[1])
#             print ('row',row,'command:',command)
       if len(bridg)==9:
        if 'br_vl_PPPoE' in bridg[3] and 'ether' in bridg[2]:
            interface_name=bridg[2].split('.')
#            pprint (interface_name)
            if interface_name[0]=='ether':
             command = '/interface vlan set name=ether1.{} numbers=[find name ~"{}"]'.format(interface_name[1],bridg[2])
             print ('row',row,'command:',command)
             show_command=send_show_command({'device_type':'cisco_ios','username':'root+ct80h100w','password':'1abrakadabra2','verbose':True,'ip':row},command)
#pprint (json.dumps(sector,ensure_ascii=False))