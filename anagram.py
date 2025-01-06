#!/usr/bin/env python3

from functools import reduce

# get_sum("act") = N = get_sum("tac")
def get_sum(word):
  #sum = reduce(lambda (x,y) : ord(x)+ord(y), list(word))
  sum=0
  for ii in list(word):
    sum=sum + ord(ii)
  return sum

# d['cat']=['tac','act']
def gen_anagram(mylist): # returns dict
  ret_dict={}
  for ii in mylist:
    tmp_list=[]
    for jj in mylist:
      if get_sum(ii)==get_sum(jj) and ii!=jj:
        tmp_list.append(jj)
    ret_dict[ii]=tmp_list
  return ret_dict

# main
mylist=["cat","sat","tas","tac","but","tub","act","ast"]
mydict=gen_anagram(mylist)
final_list=[]
for k,v in mydict.items():
  tmp_list=[]
  tmp_list.append(k)
  for ii in v:
    tmp_list.append(ii)
    tmp_list.sort()
  if tmp_list not in final_list:
    final_list.append(tmp_list)


print(final_list)
