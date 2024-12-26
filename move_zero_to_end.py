#!/usr/bin/env python3

## Given this list
list = [1,0,2,0,3,0,4,5,6]
### Write a function to modify the above list such that
## all zeros are at the end

for ii in list:
  if ii==0:
    list.remove(ii)
    list.append(ii)

print(list)
