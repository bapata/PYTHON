#!/usr/bin/env python3

import sys

## ABCD => SUM(A,B,C,D)
def to_single_digit(digit_array):
  sum=0
  for ii in digit_array:
    sum = sum + int(ii)
  return sum

# mm-dd-yyyy => ['m','m','d','d','y','y','y','y']
def to_digit_list(dob):
  components=dob.replace("-","")
  return components

# Do until we get single digit, TODO: make it recursive
def to_digit_list_wrapper(dob):
  digit_list=to_digit_list(dob)
  digit=to_single_digit(digit_list)
  if len(str(digit))>1:
    digit=to_single_digit(str(digit))
  if len(str(digit))>1:
    digit=to_single_digit(str(digit))
  return int(digit)

# main

# dd-mm-yyyy
dob=sys.argv[1]
print(dob)
print("X = " + str(to_digit_list_wrapper(dob.split("-")[0])))
print("Y = " + str(to_digit_list_wrapper(dob)))
