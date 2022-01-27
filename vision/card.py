import cv2
from card import Card, Color, Fill, Count, Shape
from set_utils import SetImg
import numpy as np

PURPLE = (137, 104, 156)
RED = (255, 107, 75)
GREEN = (80, 177, 80)

def quantImage(image,k):
    i = np.float32(image).reshape(-1,3)
    condition = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,20,1.0)
    ret,label,center = cv2.kmeans(i, k , None, condition,10,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    final_img = center[label.flatten()]
    final_img = final_img.reshape(image.shape)
    return final_img

def cropBackground(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    ## (2) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

    ## (3) Find the max-area contour
    cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv2.contourArea)[-1]

    ## (4) Crop and save it
    x,y,w,h = cv2.boundingRect(cnt)
    dst = img[y:y+h, x:x+w]
    return dst

def colorDistance(rgb1, rgb2):
    return (rgb1[0] - rgb2[0]) ** 2 + (rgb1[1] - rgb2[1]) ** 2 + (rgb1[2] - rgb2[2]) ** 2

def cardRGB(cardimage):
    nowhite = quantImage(cropBackground(cardimage), 3)
    SetImg.show(nowhite, 'fo')
    colors, count = np.unique(nowhite.reshape(-1,nowhite.shape[-1]), axis=0, return_counts=True)
    rgb = (0, 0, 0)
    whitecount = 0
    colorcount = 0
    for i in range(3):
        if not (colors[i][0] > 200 and colors[i][1] > 200 and colors[i][2] > 200):
            colorcount += count[i]
            rgb = np.add(rgb, colors[i])
        else:
            whitecount += count[i]
    return (np.divide(rgb, 2), colorcount / whitecount)

def readFill(ratio):
    if ratio > 0.9:
        return Fill.FILLED
    elif ratio > 0.3:
        return Fill.HASHED
    else:
        return Fill.EMPTY

def readColor(rgb):
    r = colorDistance(rgb, RED)
    g = colorDistance(rgb, GREEN)
    p = colorDistance(rgb, PURPLE)
    print(r, g, p)
    if  r < g and r < p:
        return Color.RED
    elif p < g and p < r:
        return Color.PURPLE
    else:
        return Color.GREEN

def detectCard(cardimage):
    rgb, ratio = cardRGB(cardimage)
    color = readColor(rgb)
    fill = readFill(ratio)
    print(color, fill)
