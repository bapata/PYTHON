#!/usr/bin/python

def power1(x,y):
  return x ** y

def power2(x,y):
  if y==0:
    return 1

  product=1
  for ii in range(y):
    product = product * x

  return product
  
def power3(x,y):
  if (y==1): 
    return x
  else:
    return x * power3(x , y-1)

print power3(2,4)

