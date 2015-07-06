#!/usr/bin/python

## Print odd and even list

def print_even_list(list):
  print "EVEN:"
  for ii in list:
    if ii%2 == 0:
      print ii

def print_odd_list(list):
  print "ODD:"
  for ii in list:
    if ii%2 != 0:
      print ii

def main():
  list=range(1,11)  
  print_odd_list(list)
  print_even_list(list)



if __name__ == "__main__":
  main()


