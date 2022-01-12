#!/usr/bin/env python3

def reverse_string(x):
  output=""
  for c in x:
    output=c+output
  return output

def reverse_string_recursion(x):
  if len(x)==1:
    return x
  else:
    return x[-1]+reverse_string_recursion(x[:-1])


# main
print(reverse_string("cricket"))
print(reverse_string_recursion("cricket"))
