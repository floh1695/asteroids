#!/usr/bin/python3

import math

class Location():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def update(self, distance, angle):
    self.x += distance * math.sin(angle.asRadians())
    self.y += distance * math.cos(angle.asRadians())

  def asList(self):
    return [self.x, self.y]
