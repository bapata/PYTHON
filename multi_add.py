#!/usr/bin/python

# Adding multiple numbers and variable number of arguments in python

def multi_add(*args):
    result=0
    for ii in args:
        result+=ii
    return result


print multi_add(1,2,3,4,5,6,7,)
