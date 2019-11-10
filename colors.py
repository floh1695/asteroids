#!/usr/bin/python3

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
