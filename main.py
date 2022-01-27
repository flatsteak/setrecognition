import PySimpleGUI as sg
from card import randomBoard, Count
from constants import WIDTH, SHAPE_WIDTH, HEIGHT, CARD_WIDTH, CARD_HEIGHT
from shapes import drawShape

currentBoard = randomBoard()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
  [sg.Graph(canvas_size=(WIDTH, HEIGHT), graph_bottom_left=(0, HEIGHT), graph_top_right=(WIDTH, 0), background_color='brown', key='graph')],
  ]

# https://pysimplegui.readthedocs.io/en/latest/call%20reference/
# https://pysimplegui.readthedocs.io/en/latest/cookbook/
# g.DrawRectangle((25,300), (100,280), line_color='purple'  )
# draw an individual card
def drawCard(g, card, x, y):
  print(card.shorthand)
  g.DrawRectangle((x + 5, y + 5), (x + WIDTH / 4 - 5, y + HEIGHT / 3 - 5), fill_color='white', line_color='white')
  c = card.systemColor
  f = card.fill
  if card.count == Count.ONE:
    drawShape(g, card.shape, x + WIDTH / 8, y + HEIGHT / 6, c, f)
  elif card.count == Count.TWO:
    drawShape(g, card.shape, x + WIDTH / 8 - SHAPE_WIDTH + 12, y + HEIGHT / 6, c, f)
    drawShape(g, card.shape, x + WIDTH / 8 + SHAPE_WIDTH - 12, y + HEIGHT / 6, c, f)
  else:
    drawShape(g, card.shape, x + WIDTH / 8, y + HEIGHT / 6, c, f)
    drawShape(g, card.shape, x + WIDTH / 8 - SHAPE_WIDTH - 5, y + HEIGHT / 6, c, f)
    drawShape(g, card.shape, x + WIDTH / 8 + SHAPE_WIDTH + 5, y + HEIGHT / 6, c, f)

def drawBoard(g, cards):
  cardX = 0
  cardY = 0
  for card in cards:
    drawCard(g, card, cardX, cardY)
    cardX = cardX + CARD_WIDTH
    if cardX >= WIDTH:
      cardY = cardY + CARD_HEIGHT
      cardX = 0

  
# Create the Window
window = sg.Window('SET Game', layout, finalize=True)

graph = window['graph']    
drawBoard(graph, currentBoard[:12])
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()