/interface vlan
add interface=ether1 loop-protect-disable-time=0s name=ether1.2006 vlan-id=2006
/interface bridge
add fast-forward=no name=br_vl_BRAS protocol-mode=none
/ip address
add address=192.168.100.1 interface=br_vl_BRAS network=192.168.100.1
/ip address
add address=10.2.2.88/24 interface=ether1.2006 network=10.2.2.0
/system identity set name=accel-ppp
/radius
add accounting-port=1815 address=192.168.0.4 authentication-port=1814 secret=ctrhtn service=ppp
/radius incoming
set accept=yes port=1814
/interface pppoe-server server
add disabled=no interface=br_vl_BRAS one-session-per-host=yes
/routing ospf area
set [ find default=yes ] disabled=yes
add area-id=0.0.0.1 default-cost=1 inject-summary-lsas=yes name=area1 type=stub
/routing ospf instance
set [ find default=yes ] redistribute-connected=as-type-1 router-id=10.2.2.88
/routing ospf interface
add interface=ether1.2006 network-type=broadcast priority=0
add network-type=broadcast passive=yes
/routing ospf network
add area=area1 network=10.2.2.0/24
add area=area1 network=10.1.0.0/19
add area=area1 network=91.197.76.0/22
