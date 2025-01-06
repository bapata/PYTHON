#!/usr/bin/env python3

# Read a CSV file and convert to dict
# The first row of CSV file contains header
# cat csv_file1.txt
# 
# ip,count
# 1.1.1.4,20
# 3.2.1.4, 44
# 6.7.4.5, 3
# 8.7.3.4,  9

import csv

mycsvfile="./csv_file1.txt"
with open(mycsvfile,"r") as fp:
  csv_as_dict = csv.DictReader(fp)
  for entry in csv_as_dict:
    print(f"IP:{entry['ip']}, COUNT:{entry['count']}")


# Output
# IP:1.1.1.4, COUNT:20
# IP:3.2.1.4, COUNT: 44
# IP:6.7.4.5, COUNT: 3
3 IP:8.7.3.4, COUNT:  9
