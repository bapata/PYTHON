#!/usr/bin/env python

import yaml
import sys

# <script> <yaml-file>

f = open(sys.argv[1])
# use safe_load instead load
dataMap = yaml.safe_load(f)
f.close()
print dataMap
