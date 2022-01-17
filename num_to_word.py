#!/usr/bin/env python3

def numberstr_to_word(numberstr):
  mappings={
	0:[''],
	1:[''],
	2:['a','b','c'],
	3:['d','e','f'],
	4:['g','h','i'],
	5:['j','k','l'],
	6:['m','n','o'],
	7:['p','q','r','s'],
	8:['t','u','v'],
	9:['w','x','y','z'],
  }
  for c in numberstr:
    char_list=mappings[ord(c)-48]
    print(char_list)

# main

numberstr="99029"
numberstr_to_word(numberstr)
