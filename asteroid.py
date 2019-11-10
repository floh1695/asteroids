#!/usr/bin/python3

from gameObject import GameObject

class Asteroid(GameObject):
  def __init__(self, location, angle, speed, health):
    GameObject.__init__(self,
      location,
      angle,
      speed)
    self.health = health

  def update(self):
    GameObject.update(self)

  def draw(self, externalSurface):
    pass
