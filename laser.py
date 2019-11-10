#!/usr/bin/python3
from gameObject import GameObject

class Laser(GameObject):
  def __init__(self, location, angle):
    GameObject.__init__(self,
      './images/laser.png',
      location,
      angle,
      1)