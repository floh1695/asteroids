#!/usr/bin/python3

import math

class Angle():
  def __init__(self, degrees):
    self.setDegrees(degrees)

  def setDegrees(self, degrees):
    self.degrees = degrees % 360

  def turnRight(self, delta):
    self.turnLeft(delta * -1)

  def turnLeft(self, delta):
    self.setDegrees(self.degrees + delta)

  def asRadians(self):
    return self.degrees * (math.pi / 180)
