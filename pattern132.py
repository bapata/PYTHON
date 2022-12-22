#!/usr/bin/env python3

def ispattern132(mylist,left_index,middle_index,right_index):
  if mylist[left_index]<mylist[middle_index] and mylist[middle_index]>mylist[right_index]:
    return True
  return False

def get_132pattern(mylist):
  lindex,mindex,rindex=0,1,2
  ret_list=[]
  while rindex<len(a):
    if ispattern132(a,lindex,mindex,rindex):
      ret_list.append(a[lindex])
      ret_list.append(a[mindex])
      ret_list.append(a[rindex])
      break
    else:
      lindex=lindex+1
      mindex=mindex+1
      rindex=rindex+1
  return ret_list

# main
#a=[3,1,4,2]
#a=[1,2,3,4]
a=[1,2,3,4,2]
print(get_132pattern(a))
