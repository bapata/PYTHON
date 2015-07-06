#!/usr/bin/python

# 
## Example script to demonstrate use of ARGC, ARGV in python
## USAGE: <this-script> 1 2 3
##        <this-script> 4 3 5 6 9
## Exepected output is sum of all arguments
#

import io, sys

# Script to test main invocation
def print_arguments(argv):
    # Count
    argc = len(argv)

    # Walk all arguments and print it
    for ii in range(argc):
        print "argv[" + str(ii) + "] is " + argv[ii]

# Input: List of integers
# Output : Sum
def sum_of_args(list):
    list_count=len(list)

    sum=0
    # Walk list and calculate sum
    for ii in range(list_count):
        sum+=list[ii]

    return sum


def main(argv):
    print "I am in main"

    print_arguments(argv)
    int_list=[int(x) for x in argv[1:]]
    sum=sum_of_args(int_list)
    print "Sum : " + str(sum)


if (__name__ == "__main__"):
    main(sys.argv)
