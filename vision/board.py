import cv2
from utils import SetImg

def blurBoard(board):
    gray = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (1, 1), 0)
    return blurred

def threshBoard(blurred):
    resultCode, thresh = cv2.threshold(blurred, 125, 200, cv2.THRESH_BINARY)
    return thresh

def contourBoard(thresh):
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = list(filter(lambda c: cv2.contourArea(c) > 10000, contours))
    print(f'Found {len(contours)} contours')
    return contours

def extractCards(path):
    board = cv2.imread(path, cv2.IMREAD_COLOR)
    board = SetImg.rotate_bound(board, 90)
    board = cv2.resize(board, (800, 600),interpolation = cv2.INTER_CUBIC)
    board = cv2.copyMakeBorder(board, 50, 50, 25, 25, cv2.BORDER_REPLICATE)
    contours = contourBoard(threshBoard(blurBoard(board)))
    l = list()
    for index, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        c = board[y+5:y + h-5, x+5:x + w-5]
        l.append(c)
        cv2.imwrite(str(index)+ '.png', c)
    return l
