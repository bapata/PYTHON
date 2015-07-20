#!/usr/bin/env python

# Script to create Hash of Hash
# after reading a file containing
# 3 fields per row

import sys

filename = sys.argv[1]
f = open (filename, "r")

# HashOfHash = { a => { c => d } }
HashOfHash={}

for line in f.readlines():
  if len(line) <=0:
    continue

  col1,col2,col3=line.rstrip('\n').split()
  # First create inner hash
  InnerHash={}
  InnerHash[col2]=col3
  # Now create outer hash
  HashOfHash[col1]=InnerHash
 

# Print the hash we constructed
print HashOfHash 
