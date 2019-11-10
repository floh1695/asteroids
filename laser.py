#!/usr/bin/python3
from gameObject import GameObject
import pygame

class Laser(GameObject):
  def __init__(self, location, angle):
    GameObject.__init__(self,
      './images/laser.png',
      location,
      angle,
      10)
    self.time = 60

  def update(self):
    GameObject.update(self)
    
    self.time -= 1
    if self.time <= 0:
      self.alive = False