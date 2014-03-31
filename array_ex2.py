#!/usr/bin/python

def main():
    team1=['tendulkar','dhoni','rohit','kohli','amarnath']

    print "several ways to print contents of array"

    print "==Method1=="
    print [ x.upper() for x in team1]
    print "==Method2=="
    for x in team1:
      print x.upper()
    print "==Method3=="
    count=len(team1)
    ii=0
    while ii<count:
      print team1[ii].upper()
      ii=ii+1

if __name__ == "__main__":
    main()
