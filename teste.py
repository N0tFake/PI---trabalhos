import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as img

img1 = cv.imread('imagens/star.png')
img2 = cv.imread('imagens/lena200.png')

# adicão
sumResult = np.zeros(shape=(200,200,3), dtype=np.uint8)
for y in range(len(img1)):
  for x in range(len(img1[0])):
    r = int(img1[y][x][0]) + int(img2[y][x][0])
    g = int(img1[y][x][1]) + int(img2[y][x][1])
    b = int(img1[y][x][2]) + int(img2[y][x][2])  
    if r > 255:
      r = 255
    if g > 255:
      g = 255
    if b > 255:
      b = 255
    
    pixel = np.array([r, g, b])
    sumResult[y][x] = pixel

# subtração
subResult = np.zeros(shape=(200,200,3), dtype=np.uint8)
for y in range(len(img1)):
  for x in range(len(img1[0])):
    r = int(img1[y][x][0]) - int(img2[y][x][0])
    g = int(img1[y][x][1]) - int(img2[y][x][1])
    b = int(img1[y][x][2]) - int(img2[y][x][2])  
    if r < 0:
      r = 0
    if g < 0:
      g = 0
    if b < 0:
      b = 0
    
    pixel = np.array([r, g, b])
    subResult[y][x] = pixel
  
  
  
""" result = cv.subtract(img1, img2)
cv.imshow('teste', result)
#cv.imshow('teste', subResult)

#cv.imshow('teste', sumResult)

if cv.waitKey(0) & 0xff == 27:
 cv.destroyAllWindows()  """