#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Speak for animals")
parser.add_argument("-n",default=0,help="number of times to speak",type=int)
parser.add_argument("-a",default="cat",help="Animal type",type=str)
args = parser.parse_args()

for _ in range(args.n):
  if args.a == "dog":
    print("woff")
  elif args.a == "cat":
    print("meow")
  else:
    print("unknown animal")
