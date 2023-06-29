#!/usr/bin/python3


import math

def factors(filename):
  with open(filename) as f:
    for line in f:
      number = int(line.strip())
      factors = []
      for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
          factors.append(i)
          number //= i
      if number > 1:
        factors.append(number)
      print(f"{number}={'*'.join(str(f) for f in factors)}")

if _name_ == "_main_":
  factors("tests/test00")
