#!/usr/bin/env python3

# Limit x->0, x-to-the-power-of-x is 1
import sys

val_list = sys.argv[1:]
for ii in val_list:
  n = float(ii)
  print(n,",",n**n)
  
  
# 0.1 , 0.7943282347242815
# 0.001 , 0.9931160484209338
# 1e-05 , 0.9998848773724686
# 1e-10 , 0.9999999976974149
# 1e-13 , 0.9999999999970066
# 1e-16 , 0.9999999999999963
# 1e-17 , 0.9999999999999996
# 1e-18 , 1.0
