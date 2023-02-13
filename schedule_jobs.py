#!/usr/bin/env python3

import schedule
import time
def mytask1():
  print("Task1")

def mytask2():
  print("Task2")

schedule.every(1).minutes.do(task1)
schedule.every(5).seconds.do(task2)
while True:
  schedule.run_pending()
  time.sleep(1)
