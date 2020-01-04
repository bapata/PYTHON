#!/usr/bin/env python

## Script to obfuscate given email address
## 

import re

def obfuscate_id(email_id):
  ret_list = []
  components = re.split(r'(\.|\@)',email_id)
  for ii in components:
    if ii=='@':
        ret_list.append("at")
    elif ii==".":
        ret_list.append("(dot)")
    else:
        ret_list.append(ii)
  return " ".join(ret_list)


def main():
  obfuscated_id = obfuscate_id("john.smith@example.com")
  print obfuscated_id

if __name__ == "__main__":
  main()
