#!/usr/bin/python

# Input=n (integer)
# if n is multiple of 3, print "foo"
# if n is multiple of 5, print "bar"
# if n is multiple of 3 and 5, print "foobar"
# print n otherwise

def foo_bar_baz(n):
  outputstr=""

  if n % 3 == 0:
    outputstr="foo"
  if n % 5 == 0:
    outputstr= outputstr + "bar"

  if outputstr != "":
    return outputstr

  return n


## main

input_list = range(1,51)
op_list = [ foo_bar_baz(k) for k in input_list ]
print op_list
