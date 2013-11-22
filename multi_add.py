#!/usr/bin/python
def multi_add(*args):
    result=0
    for ii in args:
        result+=ii
    return result


print multi_add(1,2,3,4,5,6,7,)
