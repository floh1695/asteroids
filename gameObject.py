#!/usr/bin/python3

import pygame

from location import Location
from angle import Angle
from constant import screenX, screenY

class GameObject():
  def __init__(self, image, location, angle, speed):
    self.alive = True
    self.image = image
    self.location = location
    self.angle = angle
    self.speed = speed

  def isAlive(self):
    return self.alive

  def update(self):
    self.location.update(self.speed, self.angle)

    borderRatio = 0.05
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
    surface = self.getSurface()

    externalSurface.blit(
      surface,
      self.location.asList())

  def getSurface(self):
    surface = pygame.image.load(self.image)

    rotatedSurface = pygame.transform.rotate(
      surface,
      self.angle.degrees)

    return rotatedSurface
