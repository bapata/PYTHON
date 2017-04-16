#!/usr/bin/python
## nCr computation
## <script> n r
import sys
import math

def nCr(n,r):
    fac = math.factorial
    return fac(n) / fac(r) / fac(n-r)

if __name__ == '__main__':
    n=int(sys.argv[1])
    r=int(sys.argv[2])
    #print nCr(4,2)
    print nCr(n,r)
