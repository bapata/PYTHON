#!/usr/bin/python

import sys

def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main(argv):
    n=int(argv[1])
    a=range(n)
    b=[fib(x) for x in a]
    print b

if __name__ == "__main__":
    main(sys.argv)
