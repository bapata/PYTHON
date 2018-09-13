#!/usr/bin/python

import csv
import json

# Parsing lines
# <field1>;<field2>;<field3a,field3b,field3c>
# to generate hash of the form <field1>=><field2>=>[field3a,field3b,field3c]
#
# Just run it to see the output
# ./<this-script> <csv-file>
# <csv-file> contents as below
#1.1.1.1;apple.com;192.168.1.1,192.168.1.2
#1.1.1.2;yahoo.com;172.24.1.1,172.24.1.2
#

def to_hoa(array):
  ret_hash={}
  key,value = array[0],array[1]
  value_list = value.split(',')
  ret_hash[array[0]] = value_list
  return ret_hash

def csv_to_hofh(csv_file):
  fobj = open(csv_file,'r')
  csv_obj = csv.reader(fobj,delimiter=';')
  mystore={}
  for row in csv_obj:
    mystore[row[0]]=to_hoa(row[1:])
  return mystore

def main():
  hoha = csv_to_hofh("./csv_to_hofh.txt")
  print json.dumps(hoha,indent=2)

main()
