#!/usr/bin/env python3

## List comprensions

x=1
y=1
z=1
n=3

# Print list where list[0]+list[1]+list[2]!=n
d=[(m,n,o) for m in range(x+1) for n in range(y+1) for o in range(z+1)]
e=print([[p[0],p[1],p[2]] for p in d if p[0]+p[1]+p[2]!=n])



