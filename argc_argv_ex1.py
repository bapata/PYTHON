#!/usr/bin/python
import sys

def main(argv=None):
    if(argv==None):
        argv=sys.argv
        argc=len(argv)
    print "I am in main"
    print "argc = " + str(argc)
    counter=0
    for x in argv:
        print "ARGUMENT: " + str(counter) + ":" + x
        counter = counter + 1


if (__name__ == "__main__"):
    main()
