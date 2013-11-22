#!/usr/bin/python

ctr=0
while ctr<10:
    ctr+=1
    if ctr in [2,4]:
        continue
    print "doing stuff" + str(ctr)
