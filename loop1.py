#!/usr/bin/python

# Use of range example

def main():
    x=0
    while(x<10):
        print x
        x+=1

    print "for loop example"
    for xx in range(1,11):
        print xx


    days=["sun","mon","tue"]
    for dd in days:
        print dd

    for ii,dd in enumerate(days):
        print ii,dd
    

if __name__ == "__main__":
    main()

