#!/usr/bin/python
import sys

## Kaprekar's number 6174


def high_to_low(n):
  n_as_str=str(n)
  slist = sorted(n_as_str)
  slist.reverse()
  sdigit_str = ''.join(slist)
  return int(sdigit_str)

def low_to_high(n):
  n_as_str=str(n)
  slist = sorted(n_as_str)
  sdigit_str = ''.join(slist)
  return int(sdigit_str)


# main

def main():
  if len(sys.argv)!=2:
    print "USAGE: kaprekarno.py <4-digit-number>"
    sys.exit(1)

  n=int(sys.argv[1])

  KNUM=6174
  print "You started with initial number = " + str(n)
  while(n!=KNUM):
    a=high_to_low(n)
    print "high_to_low: " + str(a)
    b=low_to_high(n)
    print "low_to_high: " + str(b)
    n=a-b
    print "intermediate number is: " + str(n)

  print "We have hit kaprekars number: " + str(n)

main()
