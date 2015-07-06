#!/usr/bin/python

a=range(5)
b=[str(x) for x in a]
c=",".join(b)

print c

fruits=['mango','orange','apple','pineapple','sapota','jackfruit','cherries']

fruits_i_like=[x for x in fruits if x not in ['cherries','pineapple']]
print fruits_i_like
