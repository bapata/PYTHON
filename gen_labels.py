#!/usr/bin/env python3
# Set AxBxC

countries=["egypt","croatia","kenya","canada"]
fruits=["apple","orange","pear"]
vegetables=["cucumber","tomato","radish","potato","garlic"]

labels=[ c +"-" + f + "-" + v for c in countries for f in fruits for v in vegetables ]
print(labels)
