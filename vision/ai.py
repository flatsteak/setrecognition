from board import extractCards
from card import detectCard

cards = extractCards('../boards/boardcontrast.png')
print(detectCard(cards[0]))
print(detectCard(cards[1]))
print(detectCard(cards[2]))
print(detectCard(cards[3]))
print(detectCard(cards[4]))
print(detectCard(cards[5]))
print(detectCard(cards[11]))