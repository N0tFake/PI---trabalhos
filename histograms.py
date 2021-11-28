from matplotlib.colors import Normalize
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def histograms(img):
    fig = plt.figure(figsize=(12, 5))
    rows = 1
    columns = 2

    fig.add_subplot(rows, columns, 1)
    plt.imshow(img)
    plt.axis('off')
    plt.title("Imagem")

    fig.add_subplot(rows, columns, 2)
    plt.hist(img.ravel(), 256, [0,256])
    plt.title("Histograma")
    
    plt.show()

def normalizeHist(img):
    weights = np.ones_like(img.ravel())/float(len(img))
    
    fig = plt.figure(figsize=(12, 5))
    rows = 1
    columns = 2
    
    fig.add_subplot(rows, columns, 1)
    plt.imshow(img)
    plt.axis('off')
    plt.title("Imagem")

    fig.add_subplot(rows, columns, 2)
    plt.hist(img.ravel(), weights=weights)
    plt.title("Histograma normalizado")
    
    plt.show()
 
def equalizeHist(img):
    imgToYuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    imgToYuv[:,:,0] = cv.equalizeHist(imgToYuv[:,:,0])
    result = cv.cvtColor(imgToYuv, cv.COLOR_YUV2BGR)
    
    fig = plt.figure(figsize=(15, 5))
    rows = 1
    columns = 3

    fig.add_subplot(rows, columns, 1)
    plt.imshow(img)
    plt.axis('off')
    plt.title("Imagem")

    fig.add_subplot(rows, columns, 2)
    plt.imshow(result)
    plt.axis('off')
    plt.title("Imagem equalizada")
    
    fig.add_subplot(rows, columns, 3)
    plt.hist(result.ravel(), 256, [0,256])
    plt.title("Histograma equalizado")
    
    plt.show()
    
def contrastStreching(img):
    xp = [0, 64, 128, 192, 255]
    fp = [0, 16, 128, 240, 255]
    x = np.arange(256)
    table = np.interp(x, xp, fp).astype('uint8')
    result = cv.LUT(img, table)
    
    #result = (img - img.min())/(img.max() - img.min())
    fig = plt.figure(figsize=(15, 5)) 
    rows = 1
    columns = 2

    fig.add_subplot(rows, columns, 1)
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Imagem")

    fig.add_subplot(rows, columns, 2)
    plt.imshow(cv.cvtColor(result, cv.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Contrast Streching - Resultado")
    
    plt.show()
