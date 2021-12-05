#!/usr/bin/env python
import functools
import sys

def is_armstrong_number(n):
  num=int(n)
  nstr=n # ensure inputed number  is in the form of  string
  mylen = len(nstr)
  n_list = [int(x) for x in nstr]
  armlist = [y**mylen for y in n_list]
  sum=functools.reduce(lambda a, b: a+b, armlist)
  return (num==sum)

# main starts here
if len(sys.argv)!=2:
  print "USAGE: <this-script> <number>"
  sys.exit(-1)

number = sys.argv[1]
if is_armstrong_number(number):
  print str(number) + " is a armstrong number"
else:
  print str(number) + " is NOT a armstrong number"
