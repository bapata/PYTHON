#!/usr/bin/python

import sys,os

def sum_of_numbers(n):
    sum=0
    for x in range(1,n+1):
        sum+=x
    return sum

def product_of_numbers(n):
    return 1 if (n<=0) else n * product_of_numbers(n - 1)

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

    if(argc!=2):
        usage()

    number=int(argv[1])

    print "Sum of 1 to " + str(number) + " is " + str(sum_of_numbers(number))
    print "\n1x2x3x.." + str(number) + " is " + str(product_of_numbers(number))


if __name__ == "__main__":
    main(sys.argv)
