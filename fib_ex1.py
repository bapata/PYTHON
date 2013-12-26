#!/usr/bin/python

def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main():
    a=range(30)
    b=[fib(x) for x in a]
    print b

if __name__ == "__main__":
    main()
