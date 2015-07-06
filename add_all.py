#!/usr/bin/python

#
## Python script to demonstrate use of variable number of arguments
#

def add_all(*args):
  sum=0
  for ii in args:
    sum = sum + ii

  return sum


def main():
  print add_all(1,2)
  print add_all(1,5,4)


if __name__ == "__main__":
  main()
  




