import cv2
import math
from matplotlib import pyplot as plt
import numpy as np

class SetImg:
  @staticmethod
  def show(img, title):
      plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
      plt.title(title)
      plt.show()

  @staticmethod
  def show_horizontal(images, titles, cols):
      fig = plt.figure(figsize=(18, 18))
      fig.tight_layout()
      number_of_files = len(images)
      for i, image in enumerate(images):
          a = fig.add_subplot(math.ceil(len(images) / cols), cols, i+1)
          plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
          plt.title(titles[i])
          plt.axis('off')

  @staticmethod
  def rotate_bound(image, angle):
      # grab the dimensions of the image and then determine the
      # center
      (h, w) = image.shape[:2]
      (cX, cY) = (w // 2, h // 2)
      # grab the rotation matrix (applying the negative of the
      # angle to rotate clockwise), then grab the sine and cosine
      # (i.e., the rotation components of the matrix)
      M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
      cos = np.abs(M[0, 0])
      sin = np.abs(M[0, 1])
      # compute the new bounding dimensions of the image
      nW = int((h * sin) + (w * cos))
      nH = int((h * cos) + (w * sin))
      # adjust the rotation matrix to take into account translation
      M[0, 2] += (nW / 2) - cX
      M[1, 2] += (nH / 2) - cY
      # perform the actual rotation and return the image
      return cv2.warpAffine(image, M, (nW, nH))

  @staticmethod
  def getSubImage(src, rect):
      # Get center, size, and angle from rect
      center, size, theta = rect
      # Convert to int
      center, size = tuple(map(int, center)), tuple(map(int, size))
      # Get rotation matrix for rectangle
      M = cv2.getRotationMatrix2D(center, theta, 1)
      # Perform rotation on src image
      dst = cv2.warpAffine(src, M, src.shape[:2])
      out = cv2.getRectSubPix(dst, size, center)
      if rect[1][1] > rect[1][0]:
          return SetImg.rotate_bound(out, 90)
      return out