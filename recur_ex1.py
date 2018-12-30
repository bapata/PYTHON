#!/usr/bin/env python

#
## Problem solving using recursion
#


#
# Sum of numbers in a list
#
def add_contents(num_list):
  if len(num_list) == 1:
    return num_list[0]
  else:
    return num_list[0]+ add_contents(num_list[1:])

# We could have just used m ** n,
# I am intentionally writing this function
# to understand recursion
def int_power(m,n):
  if n==0:
    return 1
  else:
    return m * int_power(m,n-1)

## One more version
def my_pow(x,y):
  if x==0:
    return 0
  elif x==1:
    return 1
  elif y==1:
    return x
  else:
    return x*my_pow(x,y-1)
  
def factorial(n):
  if (n==0):
    return 1
  else:
    return n * factorial(n-1)

## Sum and prod of contents in a list
# Sum of list
def sum_list(mylist):
  if len(mylist)==0:
    return 0
  elif len(mylist)==1:
    return mylist[0]
  else:
    return mylist[0]+sum_list(mylist[1:])

# Prod of a list
def prod_list(mylist):
  if len(mylist)==0:
    return 0
  elif len(mylist)==1:
    return mylist[0]
  else:
    return mylist[0]*sum_list(mylist[1:])
  
  
def main():
  a=[1,2,3]
  print add_contents(a) # Expect 6
  a=[4,5,2,1,7]
  print add_contents(a) # Expect 19

  m=2
  n=3
  print int_power(m,n) # Expect 8

  print factorial(5) # Expect 120
  print factorial(10) # Expect 3628800

#
## Main starts here
#
if __name__== "__main__":
  main()
