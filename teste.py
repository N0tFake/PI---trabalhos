import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as img

img1 = cv.imread('imagens/dente.png')
img2 = cv.imread('imagens/padrao.png')

def sum():
  result = np.zeros(shape=(len(img1),len(img1[0]),3), dtype=np.uint8)
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
      result[y][x] = pixel
  return result

def subtraction():
  result = np.zeros(shape=(len(img1),len(img1[0]),3), dtype=np.uint8)
  for y in range(len(img1)):
    for x in range(len(img1[0])):
      r = int(img1[y][x][0]) - int(img2[y][x][0])
      g = int(img1[y][x][1]) - int(img2[y][x][1])
      b = int(img1[y][x][2]) - int(img2[y][x][2])  
      if r < 0:
        r *= -1
      if g < 0:
        g *= -1
      if b < 0:
        b *= -1
      
      
      pixel = np.array([r, g, b])
      result[y][x] = pixel
  return result
  
def multiplication():
  result = np.zeros(shape=(len(img1),len(img1[0]),3), dtype=np.uint8)
  for y in range(len(img1)):
    for x in range(len(img1[0])):
      r = (( int(img1[y][x][0]) / 255 ) * ( int(img2[y][x][0]) / 255 )) * 255
      g = (( int(img1[y][x][1]) / 255 ) * ( int(img2[y][x][1]) / 255 )) * 255
      b = (( int(img1[y][x][2]) / 255 ) * ( int(img2[y][x][2]) / 255 )) * 255
      
      pixel = np.array([r, g, b])
      result[y][x] = pixel
  return result

def division():
  minR ,maxR = 0.0, 0.0
  minG ,maxG = 0.0, 0.0
  minB ,maxB = 0.0, 0.0
  result = np.zeros(shape=(len(img1),len(img1[0]),3), dtype=np.uint8)
  for y in range(len(img1)):
    for x in range(len(img1[0])):
      
      # verificando se algumas das imagens possuem uma cor com valor 0
      # caso sejá encontrado, a imagem 1 será dividida por 1
      if int(img1[y][x][0]) != 0 and int(img2[y][x][0]) != 0: 
        r = int(int(img1[y][x][0]) / int(img2[y][x][0]))
      else:
        r = int(img1[y][x][0]) / 1
        
      if int(img1[y][x][1]) != 0 and int(img2[y][x][1]) != 0: 
        g = int(int(img1[y][x][1]) / int(img2[y][x][1]))
      else:
        g = int(img1[y][x][1]) / 1
        
      if int(img1[y][x][2]) != 0 and int(img2[y][x][2]) != 0: 
        b = int(int(img1[y][x][2]) / int(img2[y][x][2]))
      else:
        b = int(img1[y][x][2]) / 1
        
      pixel = np.array([r, g, b])
      result[y][x] = pixel
      
  return cv.normalize(result,None,0,255,cv.NORM_MINMAX)



## TESTES

#result = subtraction()
#result = sum()
#result = multiplication()
#result = division()

#result = cv.divide(img1, img2) 

cv.imshow('teste', result)
if cv.waitKey(0) & 0xff == 27:
 cv.destroyAllWindows() 
