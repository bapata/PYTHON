#!/usr/bin/env python

import yaml
import sys

def flatten(nested_list):
  ret_val=set()
  for myarray in nested_list:
    for one_element in myarray:
      ret_val.add(one_element)
  return list(ret_val)

      
# Main starts here
# <script> <yaml-file>

f = open(sys.argv[1])
# use safe_load instead load
dataMap = yaml.safe_load(f)
f.close()
#print dataMap

mykeys = dataMap.keys()
companies = [ company.upper() for company in mykeys ]
print "==Company List=="
print companies

myvalues=dataMap.values()

print myvalues
country_names=[ ct.keys() for ct in myvalues ]
#print country_names 

print "==Country List=="
print flatten(country_names)

city_names=[ cty.values() for cty in myvalues ]
city_set=set()
for cty in city_names:
  mylist=flatten(cty)
  for onecity in mylist:
    city_set.add(onecity)

print "==City List=="
print list(city_set)
