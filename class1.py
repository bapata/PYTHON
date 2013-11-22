#!/usr/bin/python

class myClass1():
    def method1(self):
        print "myclass1::method1"

    def method2(self,myString):
        print "myclass1::method2"
        print myString


class myClass2(myClass1):
    def method1(self):
        print myClass1.method1(self)
        print "myClass2::method1"

    def method2(self,myString):
        print "myClass2::method2"
#        print myClass1.method2(self,myString)
        print myString


def main():
    obj1=myClass1()
    obj1.method1()
    obj1.method2("yahoo")

    obj2=myClass2()
    obj2.method1()
    obj2.method2("sunnyvale")


if (__name__ == "__main__"):
    main()
    
