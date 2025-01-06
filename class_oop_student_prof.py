#!/usr/bin/env python3

# demo program for OOP in python

class Wizard:
  def __init__(self,name):
    self.name = name


class Student(Wizard):
  def __init__(self,name,loc):
    super().__init__(name)
    self.loc = loc
  def __str__(self):
    return f"{self.name} lives at {self.loc}"

class Professor(Wizard):
  def __init__(self,name,subject):
    super().__init__(name)
    self.subject = subject
  def __str__(self):
    return f"{self.name} teaches {self.subject}"


# main

s = Student("atul","sjc")
p = Professor("Vivek", "math")
print(s)
print(p)
