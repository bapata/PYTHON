#!/usr/bin/python

# Program to show minimum number of coins required given cents as input
# USAGE: <this-script> <cent-value>
# Example: ./min_coins.py 31

import sys
# 25-cents: Quarters
# 10-cents: Dime
# 5-cents:  Nickels
# 1-cents:  Pennies

def min_coins(cents):
  coin_dict = {'Q':0,'D':0,'N':0,'P':0}
  QV=25
  DV=10
  NV=5
  PV=1

  while cents!=0:
    quarter_count = cents/QV
    if quarter_count > 0:
      coin_dict['Q'] = coin_dict['Q'] + quarter_count
    cents = cents - (quarter_count * QV)

    dime_count = cents/DV
    if dime_count > 0:
      coin_dict['D'] = coin_dict['D'] + dime_count
    cents = cents - (dime_count * DV)

    nickel_count = cents/NV
    if nickel_count > 0:
      coin_dict['N'] = coin_dict['N'] + nickel_count
    cents = cents - (nickel_count * NV)

    penny_count = cents/PV
    if penny_count > 0:
      coin_dict['P'] = coin_dict['P'] + penny_count
    cents = cents - (penny_count * PV)

  return coin_dict

def print_coins(coins_dict):
  char_to_coin={'Q':'quarters(25)','D':'dimes(10)','N':'nickels(5)','P':'pennies(1)'}
  for coin_type,coin_count in coins_dict.iteritems():
    print str(coin_count) + " " + char_to_coin[coin_type]

def usage():
  print "USAGE: " + sys.argv[0] + " <number-of-cents>\n"
  sys.exit(1)

# main
if len(sys.argv)!= 2:
  usage()

print_coins(min_coins(int(sys.argv[1])))
