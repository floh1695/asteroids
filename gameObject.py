#!/usr/bin/python3

from location import Location
from angle import Angle
from constant import screenX, screenY

class GameObject():
  def __init__(self, location, angle, speed):
    self.location = location
    self.angle = angle
    self.speed = speed

  def update(self):
    self.location.update(self.speed, self.angle)

    borderRatio = 0.1
    borderX = borderRatio * screenX
    borderY = borderRatio * screenY

    if self.location.x < (0 - borderX):
      self.location.x = screenX + (borderX / 2)
    if self.location.x > (screenX + borderX):
      self.location.x = 0 - (borderX / 2)

    if self.location.y < (0 - borderY):
      self.location.y = screenY + (borderY / 2)
    if self.location.y > (screenY + borderY):
      self.location.y = 0 - (borderY / 2)

  def draw(self, externalSurface):
    print('WARN: call to default draw')
