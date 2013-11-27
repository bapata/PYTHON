#!/usr/bin/python

#
## Script to calculate summation and factorial of N
# ./sigma_and_pi.py 10
# Summation of 10 is 55
# Factorial of 10 is 3628800
#

import sys,os

def sum_upto_n(n):
    return 0 if (n<0) else n + sum_upto_n(n-1)

def product_upto_n(n):
    return 1 if (n<=0) else n * product_upto_n(n - 1)

#
## main starts here
#

def usage():
    # program name
    myscriptname=os.path.basename(__file__)
    print "USAGE: " + myscriptname + " <integer>"
    exit(1)

def main(argv):
    argc=len(argv)

    # ARGV[1] = program name
    # ARGV[2] = N
    if(argc!=2):
        usage()

    number=int(argv[1])

    print "Summation of " + str(number) + " is " + str(sum_upto_n(number))
    print "Factorial of " + str(number) + " is " + str(product_upto_n(number))


if __name__ == "__main__":
    main(sys.argv)
