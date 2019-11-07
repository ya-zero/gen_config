# -*- coding: utf-8 -*-
from librouteros import connect
from pprint import pprint


api = connect(username='root',password='1abrakadabra2',host='192.168.30.3')
pprint(api(cmd='/interface/print', stats=True))
#pprint(api(cmd='/ip/address/print', stats=True))
api.close()