from constants import SHAPE_WIDTH, SHAPE_HEIGHT
from card import Fill, Shape

def drawSquiggle(g, color, fill, x, y):
  if fill == Fill.FILLED:
    g.DrawRectangle((x, y), (x+SHAPE_WIDTH, y+SHAPE_HEIGHT), fill_color = color, line_color = color)
  elif fill == Fill.HASHED:
    g.DrawRectangle((x, y), (x+SHAPE_WIDTH, y+SHAPE_HEIGHT), fill_color = color, line_color = 'black')
  else:
    g.DrawRectangle((x, y), (x+SHAPE_WIDTH, y+SHAPE_HEIGHT), fill_color = 'white', line_color = color)
    
def drawOval(g, color, fill, x, y):
  if fill == Fill.FILLED:
    g.DrawOval((x, y), (x+SHAPE_WIDTH, y+SHAPE_HEIGHT), fill_color = color, line_color = color)
  elif fill == Fill.HASHED:
    g.DrawOval((x, y), (x+SHAPE_WIDTH, y+SHAPE_HEIGHT), fill_color = color, line_color = 'black')
  else:
    g.DrawOval((x, y), (x+SHAPE_WIDTH, y+SHAPE_HEIGHT), fill_color = 'white', line_color = color)
  
def drawDiamond(g, color, fill, x, y):
  if fill == Fill.FILLED:
    g.DrawPolygon(((x, y+SHAPE_HEIGHT/2), (x+SHAPE_WIDTH/2, y+SHAPE_HEIGHT), (x+SHAPE_WIDTH, y+SHAPE_HEIGHT/2), (x+SHAPE_WIDTH/2, y), (x, y+SHAPE_HEIGHT/2)), fill_color = color)
  elif fill == Fill.HASHED:
    g.DrawPolygon(((x, y+SHAPE_HEIGHT/2), (x+SHAPE_WIDTH/2, y+SHAPE_HEIGHT), (x+SHAPE_WIDTH, y+SHAPE_HEIGHT/2), (x+SHAPE_WIDTH/2, y), (x, y+SHAPE_HEIGHT/2)), fill_color = color, line_color = 'black')
  else:
    g.DrawPolygon(((x, y+SHAPE_HEIGHT/2), (x+SHAPE_WIDTH/2, y+SHAPE_HEIGHT), (x+SHAPE_WIDTH, y+SHAPE_HEIGHT/2), (x+SHAPE_WIDTH/2, y), (x, y+SHAPE_HEIGHT/2)), fill_color = 'white', line_color = color)

def drawShape(g, shape, centerX, centerY, color, fill):
  x = centerX - SHAPE_WIDTH / 2
  y = centerY - SHAPE_HEIGHT / 2
  if shape == Shape.SQUIGGLE:
    drawSquiggle(g, color, fill, x, y)
  elif shape == Shape.OVAL:
    drawOval(g, color, fill, x, y)
  else:
    drawDiamond(g, color, fill, x, y)
  