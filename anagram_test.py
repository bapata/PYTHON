#!/usr/bin/env python3
from functools import reduce

# ("cat","act") true
# ("rat","act") false
def anagram_cmp(s1,s2):
  s1_list=[ord(x) for x in list(s1)]
  s2_list=[ord(y) for y in list(s2)]
  sum1=reduce(lambda x, y: (x + y), s1_list)
  sum2=reduce(lambda x, y: (x + y), s2_list)
  return sum1==sum2

def get_anagram(s1,slist):
  ret_list=[]
  for x in slist:
    if x==s1:
      continue
    if anagram_cmp(s1,x):
      ret_list.append(x)
  return ret_list


def main():
  test_list=["cat","rat","tac","act"]
  anagram_list={}
  for x in test_list:
    anagram_list[x]=get_anagram(x,test_list)
  print(anagram_list)

main()
