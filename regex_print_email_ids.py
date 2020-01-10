#!/usr/bin/env python
import sys
import re

## Print line containing email addresses
with open(sys.argv[1]) as fp:
  for line in fp.readlines():
    #print "line is {}".format(line)
    #print "Chomping ..."
    line = line.rstrip()
    #print line.split(",")
    m = re.match(r"(\S+)(\@)(\S+)",line)
    if m:
      print line
