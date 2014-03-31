#!/usr/bin/python

class Employee():
  def __init__(self,name,state,category):
    self._name=name
    self._state=state
    self._category=category

  def to_yaml(self):
    print self._name + ":"
    print "  -" + " state: " + self._state
    print "  -" + " category: " + self._category

  def to_csv(self):
    print self._name + "," + self._state + "," + self._category


def main():
  elist=[]
  static_list=[ [ "gavaskar","mh","batsman"],["kapil","hn","allrounder"],["dhoni","jh","wkeeper"], ]

  ii=0
  count=len(static_list)

  while ii<count:
    elist.append(Employee(static_list[ii][0],static_list[ii][1], static_list[ii][2]))
    ii=ii+1

  no_of_players=len(elist)

  jj=0
  while jj<no_of_players:
    elist[jj].to_yaml()
    #elist[jj].to_csv()
    jj=jj+1
  


if (__name__ == "__main__"):
    main()
    
