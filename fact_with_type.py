#!/usr/bin/env python3
import typing

# 3.9 and above supports typing

def fact_with_type(n: int) -> int:
  if n<=0:
    return 1
  else:
    return n*fact_with_type(n-1)


# main

print(fact_with_type(10))
try:
  print(fact_with_type("10.0"))
except TypeError as e:
  print("MyError: This indicates that type is properly handled")
  print(e)
