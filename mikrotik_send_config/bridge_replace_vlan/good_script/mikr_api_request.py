# -*- coding: utf-8 -*-
from librouteros import connect
from pprint import pprint
import ipaddress
import subprocess
import logging

logging.basicConfig(filename='test.log',level=logging.DEBUG)
for host_i in ipaddress.ip_network('192.168.30.100/32'):
     if subprocess.run(['ping',str(host_i),'-c','1','-W','1'],stdout=subprocess.DEVNULL).returncode == 0:
      try:
        api = connect(username='root',password='1abrakadabra2',host=str(host_i))
        cmd=('/interface/bridge/port/print')
        result=api(cmd)
        for i in result:
            print (i['bridge'],i['interface'],i['disabled'])
        api.close()
      except:
        print ('no auth')