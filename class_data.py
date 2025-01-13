#!/usr/bin/env python3

class Base:
  def __init__(self,z=0):
    self.z=z
  def __repr__(self):
    print("Base:Invoked repr")
    return f'Z={self.z}'
  def __str__(self):
    print("Invoked str")
    return f'Z={self.z}'

class Foo(Base):
  def __init__(self,x=0,y=0,z=0):
    self.x=x
    self.y=y
    super().__init__(z)
  def __repr__(self):
    print("Invoked repr")
    return f'X={self.x}, Y={self.y},Z={self.z}'
  def __str__(self):
    print("Invoked str")
    return f'X={self.x}, Y={self.y},Z={self.z}'

# main

a = Foo(1,2,3)
b = [Base(1),Foo(2,3,4)]
print(a)
print(repr(a))
print(b)
for obj in b:
  print(obj)
