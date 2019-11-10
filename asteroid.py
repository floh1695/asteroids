#!/usr/bin/python3

import pygame

from gameObject import GameObject

class Asteroid(GameObject):
  def __init__(self, location, angle, speed, level):
    GameObject.__init__(self,
      './images/asteroid.png',
      location,
      angle,
      speed)
    self.level = level
    self.health = level

  def getSurface(self):
    surface = GameObject.getSurface(self)

    healthRatio = self.health / self.level
    edge = 16 * int(self.level - healthRatio)
    newSize = (edge, edge)
    scaledSurface = pygame.transform.scale(surface, newSize)

    return scaledSurface
