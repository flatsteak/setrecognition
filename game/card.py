import random
from dataclasses import dataclass
from enum import Enum

class Color(Enum):
  RED = 'R'
  GREEN = 'G'
  PURPLE = 'P'

class Shape(Enum):
  DIAMOND = 'D'
  OVAL = 'O'
  SQUIGGLE = '~'

class Fill(Enum):
  EMPTY = '_'
  HASHED = '#'
  FILLED = '*'

class Count(Enum):
  ONE = 1
  TWO = 2
  THREE = 3

@dataclass
class Card:
    color: Color
    shape: Shape
    fill: Fill
    count: Count

    @property
    def shorthand(self) -> str:
      return f'{self.color.value}{self.shape.value}{self.fill.value}{self.count.value}'

    @property
    def systemColor(self):
      if self.color == Color.RED:
        return "red"
      elif self.color == Color.PURPLE:
        return "purple"
      return "green"
      
def MakeCard(shorthand):
  return Card(
    Color(shorthand[0]),
    Shape(shorthand[1]),
    Fill(shorthand[2]),
    Count(int(shorthand[3])),
  )

# will return all possible cards in a list
def allCards():
  deck = list()
  for s in Shape:
    for c in Color:
      for n in Count:
        for f in Fill:
          deck.append(Card(c, s, f, n))
  return deck

def randomBoard():
  deck = allCards();
  random.shuffle(deck)
  return deck
