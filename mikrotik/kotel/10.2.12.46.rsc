/interface vlan
add interface=ether1 loop-protect-disable-time=0s name=ether1.2016 vlan-id=2016

/interface bridge
add fast-forward=no name=br_vl_BRAS protocol-mode=none

/ip address
add address=192.168.100.1 interface=br_vl_BRAS network=192.168.100.1
add address=10.2.12.46/24 interface=ether1.2016 network=10.2.12.0

/system identity
set name=accel-ppp

/radius
add accounting-port=1815 address=192.168.0.4 authentication-port=1814 secret=ctrhtn service=ppp

/radius incoming
set accept=yes port=1814

/interface pppoe-server server
add disabled=no interface=br_vl_BRAS one-session-per-host=no

/ppp profile
set *0 dns-server=8.8.8.8,8.8.4.4 local-address=192.168.100.1 only-one=yes rate-limit=1M/1M \
    use-compression=no use-encryption=no use-mpls=no

/ppp aaa
set use-radius=yes

/routing ospf area
set [ find default=yes ] disabled=yes
add area-id=0.0.0.11 default-cost=1 inject-summary-lsas=yes name=area11 type=stub
/routing ospf instance
set [ find default=yes ] redistribute-connected=as-type-1 router-id=10.2.12.46
/routing ospf interface
add interface=ether1.2016 network-type=broadcast priority=0
add network-type=broadcast passive=yes
/routing ospf network
add area=area11 network=10.2.12.0/24
add area=area11 network=10.1.0.0/19
add area=area11 network=91.197.76.0/22
/ip firewall filter disable    [find where chain=forward]
/interface bridge port set bridge=br_vl_BRAS [find interface=wlan1.375]

/interface bridge filter set chain=input in-bridge=br_vl_BRAS    [find where  chain=forward]
