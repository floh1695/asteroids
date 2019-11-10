#!/usr/bin/python3

from gameObject import GameObject

from location import Location
from angle import Angle
from constant import screenX, screenY
from laser import Laser

class Player(GameObject):
  def __init__(self):
    GameObject.__init__(self,
      './images/player.png',
      Location(screenX / 2, screenY / 2),
      Angle(0),
      0)

    self.lives = 3
    self.health = 3

  def shoot(self):
    return Laser(
      Location(screenX / 2, screenY / 2),
      Angle(0))

  def forward(self):
    self.speed += 0.75

  def reverse(self):
    self.speed -= .25

  def turnRight(self):
    self.angle.turnRight(360 / 60)

  def turnLeft(self):
    self.angle.turnLeft(360 / 60)

  def update(self):
    GameObject.update(self)
    self.speed = self.speed * 0.90

  def collisionWithAsteroid(self, asteroid):
    pass
