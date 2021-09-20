#!/usr/bin/env python3

# USAGE: <this-script> <subnet> <ipAddress>

# Examples:
# $ ./is_ip_in_subnet.py 192.168.8.0/24 192.168.8.1
# 192.168.8.1 is part of subnet 192.168.8.0/24
#
# $ ./is_ip_in_subnet.py 192.168.8.0/24 192.168.9.1
# 192.168.9.1 is NOT part of subnet 192.168.8.0/24
#

import sys
import ipaddress

(mysubnet, myip) = sys.argv[1:]

ip_in_subnet = ipaddress.ip_address(myip) in ipaddress.ip_network(mysubnet)
if ip_in_subnet:
  print(myip,"is part of subnet",mysubnet)
else:
  print(myip,"is NOT part of subnet",mysubnet)
