#!/usr/bin/env python

#{   'continents': [   {   'Africa': ['Ghana', 'Kenya', 'Egypt', 'Morocco']},
#                      {   'Asia': [   'India',
#                                      'Singapore',
#                                      'SouthKorea',
#                                      'Srilanka']},
#                      {   'Europe': ['France', 'Italy']},
#                      {   'NorthAmerica': ['USA', 'Mexico']},
#                      {   'SouthAmerica': ['Brazil', 'Peru']},
#                      {   'Antartica': None},
#                      {   'Australia': None}]}

import yaml
import sys
import pprint

def main():
  my_yaml_file = sys.argv[1]
  my_dict={}
  with open(my_yaml_file) as myf:
    my_dict = yaml.load(myf,Loader=yaml.FullLoader)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(my_dict)
  print my_dict['continents'][3]['NorthAmerica'][1]

main()
