#!/usr/bin/env python3
# Move x to the end
# x is in the list
def move_x_to_end(list,x):
  for ii in list:
    if ii==x:
      list.remove(ii)
      list.append(ii)
  return list

# Given this list
list = [1,0,2,0,3,0,1,4,5,6]

# Write a function to modify the above list such that
# all x are at the end

list1=move_x_to_end(list,0)
print(list1)

list2=move_x_to_end(list,1)
print(list2)
