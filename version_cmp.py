#!/usr/bin/env python3


def ver_cmp(ver1,ver2):
    ver1_list=[int(x) for x in ver1.split(".")]
    ver2_list=[int(x) for x in ver2.split(".")]
    # List comparison
    if (ver1_list > ver2_list):
        return 1
    elif (ver1_list < ver2_list):
        return -1
    else:
        return 0


# main
version_list=["0.1","1.1","1.2","1.2.9.9.9.9","1.3","1.3.4","1.10"]
# "1.2" < "1.10" and so on
for ver1 in version_list:
    for ver2 in version_list:
        print("Comparing: "+"("+ver1+")"+" and ("+ver2+")")
        result = ver_cmp(ver1,ver2)
        if result==0:
            print(ver1+"=="+ver2)
        elif result==-1:
            print(ver1+"<"+ver2)
        else:
            print(ver1+">"+ver2)
