#!/usr/bin/env python
import collections

word='mississippi' # misp (expected)
chars=list(word)
uniq_chars=collections.OrderedDict.fromkeys(chars)
print(''.join(list(uniq_chars))) # misp
