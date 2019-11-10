#!/usr/bin/python3

import random

from asteroid import Asteroid
from location import Location
from angle import Angle
from constant import screenX, screenY
from randomtools import randfloat

class RandomAsteroid(Asteroid):
  def __init__(self, level):
    location = Location(
      randfloat(screenX),
      randfloat(screenY))
    angle = Angle(randfloat(360))
    speed = randfloat(1, 3)

    Asteroid.__init__(self,
      location,
      angle,
      speed,
      level)
