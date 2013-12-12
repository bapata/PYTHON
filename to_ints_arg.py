#!/usr/bin/env python

def to_ints_arg(init_number, *ints):
    return [init_number + int(x) for x in ints]


# main

print to_ints_arg(89,10,11,12)
