#!/usr/bin/env python3

import sys


def numberstr_to_word(numberstr):
  mappings={
	0:['0'],
	1:['1'],
	2:['a','b','c'],
	3:['d','e','f'],
	4:['g','h','i'],
	5:['j','k','l'],
	6:['m','n','o'],
	7:['p','q','r','s'],
	8:['t','u','v'],
	9:['w','x','y','z'],
  }
  ac_list=[]
  for c in numberstr:
    char_list=mappings[ord(c)-48]
    ac_list.append(char_list)

  string_list=[ ''.join([x0,x1,x2,x3,x4,x5,x6,x7,x8,x9]) for x0 in ac_list[0] for x1 in ac_list[1] for x2 in ac_list[2] for x3 in ac_list[3] for x4 in ac_list[4] for x5 in ac_list[5] for x6 in ac_list[6] for x7 in ac_list[7] for x8 in ac_list[8] for x9 in ac_list[9] ]

  for ii in string_list:
    print(ii)
# main

numberstr=sys.argv[1]
numberstr_to_word(numberstr)
