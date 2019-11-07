# -*- coding: utf-8 -*-
# выполнение комманд из file_config
# на устройствах из devices.yaml
import netmiko
import logging
from pprint import pprint

# выполнение комманд
def send_show_command(device,commands):
     result='empty'
     try:
       with netmiko.ConnectHandler(ip=device,device_type='cisco_ios',username='root',password='1abrakadabra2',verbose=True) as ssh:
            ssh.set_base_prompt(pri_prompt_terminator=u'>', alt_prompt_terminator=u'#', delay_factor=1)
#            print ('find prompt',ssh.find_prompt())
            result=ssh.send_commnad(commands,strip_command=False, strip_prompt=Fals)
            print('commands:',result)
     except:
           print('error')
     if result:
        return {device:result}

logging.basicConfig(filename='test.log',level=logging.DEBUG)
logger=logging.getLogger("netmiko")
command = 'interface print'
devices=['192.168.30.20','192.168.30.29']
for dev in  devices:
     show_command=send_show_command(dev,command)
     pprint(show_command)