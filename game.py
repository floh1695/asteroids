#!/usr/bin/python3

import pygame

from colors import color
from gameObject import GameObject
from player import Player
from randomAsteroid import RandomAsteroid
from constant import screenSize

class Game():
  def __init__(self):
    self.level = 1
    self.ticks = 0
    self.player = Player()
    self.asteroids = [
      RandomAsteroid(1),
      RandomAsteroid(2),
      RandomAsteroid(3),
      RandomAsteroid(4)]
    self.lasers = []
    self.running = False

  def play(self):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(screenSize)
    self.running = True
    while self.running:
      clock.tick(60)
      self.ticks += 1
      self.handleEvents()
      self.handleInput()
      self.handleUpdates()
      self.handleDeaths()
      self.handleCollisions()
      self.handleDrawing(screen)

  def allGameObjects(self):
    return [self.player] + self.asteroids + self.lasers

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        return

  def handleInput(self):
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_ESCAPE]:
      self.running = False
      return

    if pressed[pygame.K_SPACE]:
      laser = self.player.shoot()
      self.lasers.append(laser)

    if pressed[pygame.K_UP]:
      self.player.forward()
    if pressed[pygame.K_DOWN]:
      self.player.reverse()

    if pressed[pygame.K_RIGHT]:
      self.player.turnRight()
    if pressed[pygame.K_LEFT]:
      self.player.turnLeft()

  def handleUpdates(self):
    for gameObject in self.allGameObjects():
      gameObject.update()

  def handleDeaths(self):
    alive = GameObject.isAlive

    self.asteroids = list(filter(alive, self.asteroids))
    self.lasers = list(filter(alive, self.lasers))

  def handleCollisions(self):
    for asteroid in self.asteroids:
      self.player.collisionWithAsteroid(asteroid)

    for laser in self.lasers:
      for asteroid in self.asteroids:
        asteroid.collisionWithLaser(laser)

  def handleDrawing(self, surface):
    surface.fill(color('black'))

    for gameObject in self.allGameObjects():
      gameObject.draw(surface)

    pygame.display.flip()