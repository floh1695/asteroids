#!/usr/bin/python3

import math
import pygame

screenX = 600
screenY = 600
screenSize = [screenX, screenY]

colors = {
  'black': (  0,   0,   0),
  'white': (255, 255, 255)
}
def color(color_code):
  if color_code in colors:
    return colors[color_code]
  else:
    print(f'WARN: color code ({color_code}) is invalid')
    return colors['white']

class Location():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def update(self, distance, angle):
    self.x += distance * math.sin(angle.asRadians())
    self.y += distance * math.cos(angle.asRadians())

  def asList(self):
    return [self.x, self.y]

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

class Player():
  def __init__(self):
    self.lives = 3
    self.health = 3
    self.location = Location(screenX // 2, screenY // 2)
    self.speed = 0
    self.angle = Angle(0)

  def forward(self):
    self.speed += 0.75

  def reverse(self):
    self.speed -= .25

  def turnRight(self):
    self.angle.turnRight(360 / 60)

  def turnLeft(self):
    self.angle.turnLeft(360 / 60)

  def update(self):
    self.location.update(self.speed, self.angle)
    self.speed = self.speed * 0.90

  def draw(self, externalSurface):
    surface = pygame.image.load('./images/player.png')
    rotatedSurface = pygame.transform.rotate(
      surface,
      self.angle.degrees)

    externalSurface.blit(
      rotatedSurface,
      self.location.asList())

class Game():
  def __init__(self):
    self.level = 1
    self.ticks = 0
    self.player = Player()
    self.asteroids = []
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
      self.handleDrawing(screen)

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

    if pressed[pygame.K_UP]:
      self.player.forward()
    if pressed[pygame.K_DOWN]:
      self.player.reverse()

    if pressed[pygame.K_RIGHT]:
      self.player.turnRight()
    if pressed[pygame.K_LEFT]:
      self.player.turnLeft()

  def handleUpdates(self):
    self.player.update()
    for asteroid in self.asteroids:
      asteroid.update()

  def handleDrawing(self, surface):
    surface.fill(color('black'))

    self.player.draw(surface)
    for asteroid in self.asteroids:
      asteroid.draw(surface)

    pygame.display.flip()

def main():
  game = Game()
  game.play()

if __name__ == '__main__':
  main()
