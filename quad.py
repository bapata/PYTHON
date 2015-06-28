#!/usr/bin/python

import math

a=5
b=3
c=-1

x1 = ( -b + math.sqrt( b*b - 4*a*c) ) / (2 * a)
x2 = ( -b - math.sqrt( b*b - 4*a*c) ) / (2 * a)

print "X1 = " + str(x1)
print "X2 = " + str(x2)
