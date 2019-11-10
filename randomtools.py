#!/usr/bin/python3

import random

def randfloat(a, b=None):
  r = random.random()

  if b == None:
    return r * a
  else:
    c = b - a
    return a + (r * c)
