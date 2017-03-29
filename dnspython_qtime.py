#!/usr/bin/env python

# Prints response time

import dns.message
import dns.query
import sys

if len(sys.argv)!=3:
  print "USAGE: <script> <record> <name_server>"
  exit(1)

domain,name_server = sys.argv[1],sys.argv[2]
if len(sys.argv)==3:
  if sys.argv[2]:
    name_server = sys.argv[2]

query = dns.message.make_query(domain, dns.rdatatype.A)
response = dns.query.udp(query, name_server)
print str(response.time * 1000) + " seconds"
