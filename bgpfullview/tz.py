import re
import copy
from ipaddress import *
from sys import argv
import sqlite3

# Network            Next Hop            Metric LocPrf Weight Path
#*  0.0.0.0/0          94.156.252.18            0      0      0 34224 3356 i

def sqlite_connect():
       try:
          connection = sqlite3.connect('bgpfullview.db')
          return connection
       except sqlite3.IntegrityError as e:
            print('Error occured: ', e)

def create_table():
       connection=sqlite_connect()
       try:
            connection.execute('''create table  if not exists network
                (network text unique on conflict ignore, as_system text)'''
                )
       except sqlite3.IntegrityError as e:
            print('Error occured: ', e)


def sqlite_insert(data,as_num):
   con=sqlite_connect()
   print ('con',con)
   for i in data:
     ins = (i,as_num)
     try:
       with con:
         query = 'INSERT into network values (?, ?)'
         con.execute(query,ins)

     except sqlite3.IntegrityError as e:
            print('Error occured: ', e)


#def sqlite_select():


as_num = argv [2]
filename = argv[1]
ip_networks=[]
with open (filename,'r') as  bgpfull:
   for  i in bgpfull:
     result=re.split(r' +',i)
     if result[0] == '*': 
      if as_num in result[-2]:
        ip_networks.append(result[1])
   ip_networks=set(ip_networks)
   ip_result=copy.deepcopy(list(ip_networks))
   new_result=copy.deepcopy(list(ip_networks))
   ip_network_pref_del=copy.deepcopy(list(ip_networks))
   for ip_f  in ip_result:
      for ip_s in new_result:
          a=ip_network(ip_f) 
          b=ip_network(ip_s)
          if  a.subnet_of(b) and a != b:
              ip_network_pref_del.remove(str(a))

print (len(ip_network_pref_del))
create_table()
sqlite_insert(ip_network_pref_del,as_num)

