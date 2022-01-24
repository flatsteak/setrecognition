from card import Card, Color, Shape, Fill, Count, MakeCard
import random
import 

card1 = Card(Color.RED, Shape.OVAL, Fill.FILLED, Count.THREE)
card2 = MakeCard('RO*3')
card3 = Card(Color.RED, Shape.OVAL, Fill.FILLED, Count.THREE)

def isSame(values):
  return all(item == values[0] for item in values)
  
def areUnique(values):
  return len(set(values)) == len(values)

def isSameOrUnique(values):
  return isSame(values) or areUnique(values)

def isSet(cards):
  return isSameOrUnique(list(map(lambda c: c.color, cards))) and \
    isSameOrUnique(list(map(lambda c: c.fill, cards))) and \
    isSameOrUnique(list(map(lambda c: c.shape, cards))) and \
    isSameOrUnique(list(map(lambda c: c.count, cards)))

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

def allSets(cards):
  l = len(cards)
  for card1Index, card1 in enumerate(cards[:l-2]):
    for card2Index, card2 in enumerate(cards[card1Index+1:l-1]):
      for card3 in cards[card2Index+1:]:
        if isSet((card1, card2, card3)):
          print(card1.shorthand, card2.shorthand, card3.shorthand)
    
allSets(randomBoard()[:12])

def describeCard(card):
  