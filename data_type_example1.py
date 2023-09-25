#!/usr/bin/env python3

import collections

def count_living_per_year(population: list[tuple[int,int]]) -> dict[int,int]:
  return collections.Counter(
    year for birth,death in population for year in range(birth,death)
  )


# main
mylist=[ (1,2), (2,3) ]
print(count_living_per_year(mylist))
