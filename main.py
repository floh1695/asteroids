#!/usr/bin/python3

from game import Game

def main():
  game = Game()
  game.play()

if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    print(e)
    input('Press any key to exit')