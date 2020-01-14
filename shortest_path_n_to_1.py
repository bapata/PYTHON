#!/usr/bin/env python
import sys

## Shortest path to 1 from N with following rule:
# if a*b == N, pick N = max(a,b)
# else N = N-1

# Get list of factors for N
def get_factors(n):
  ret_list=[]
  for ii in range(1, n + 1):
    if n % ii == 0:
      ret_list.append(ii)
  return ret_list

def max(a,b):
  return a if a>b else b

def mid_point(mylist):
  list_len = len(mylist)
  if list_len%2==0:
    return max(mylist[list_len/2],mylist[list_len/2 - 1])
  else:
    return mylist[list_len/2]


# Main
out_list=[]
mp = int(sys.argv[1])
while mp>1:
  out_list.append(mp)
  fact_list = get_factors(mp)
  #print fact_list
  if fact_list[0]==1 and fact_list[1]==mp:
    mp = mp - 1
  else:
    mp = mid_point(fact_list)
out_list.append(mp)

# Print shortest path from N to 1 (buggy: 10 5 4 2 1 shd be 10 9 3 2 1)
print out_list
