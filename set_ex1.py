#!/usr/bin/env python

# How to use sets in python

from sets import Set

a=['one','two','four']
b=['one','three','four','five']

setA=Set(a)
setB=Set(b)

print "SET A is : " 
print setA

print "SET B is : " 
print setB

print "Union of A and B is :"
# setAB=setA | setB
setAB=setA.union(setB)
print setAB

print "Intersection of A and B is :"
# setAB=setA & setB
setAB=setA.intersection(setB)
print setAB

print "Difference : A - B is :"
# setAB=setA - setB
setAB=setA.difference(setB)
print setAB

print "Difference : B - A is :"
# setAB=SetB - setA
setAB=setB.difference(setA)
print setAB
