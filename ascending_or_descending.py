#!/usr/bin/env python3

nums1 =  [1, 2, 3, 4, 4, 5] # expect true
nums2 =  [7, 6, 3]  # expect true
nums3 =  [8, 4, 6]  # expect false


# Returns True if list is sorted in ascending order
#         False otherwise
def mono_incr(mylist):
  sorted_ascending=True
  for index in range(len(mylist)-1):
    if mylist[index]>mylist[index+1]:
      sorted_ascending=False
  return sorted_ascending

# Returns True if list is sorted in descending order
#         False otherwise
def mono_decr(mylist):
  sorted_descending=True
  for index in range(len(mylist)-1):
    if mylist[index]<mylist[index+1]:
      sorted_descending=False
  return sorted_descending

# Returns True if list is sorted in either ascending or descending order
#         False otherwise (not sorted at all)
def mono_incr_or_decr(mylist):
  return mono_incr(mylist) or mono_decr(mylist)

# main
print(nums1)
print(mono_incr_or_decr(nums1)) # True
print()
print(nums2)
print(mono_incr_or_decr(nums2)) # True
print()
print(nums3)
print(mono_incr_or_decr(nums3)) # False
print()
