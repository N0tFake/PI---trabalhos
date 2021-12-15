import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from arithmetic_operations import subtraction

def laplacian(img):
    kernelSize = 3
    scale = 1
    delta = 0
    result = cv.Laplacian(img, -1, ksize=kernelSize, scale=scale, delta=delta)
    return result

def LoG(img, sigma):
    kernelSize = 5
    scale = 1
    delta = 0
    ddepth = cv.CV_16S
    
    img = cv.GaussianBlur(img, (5,5), sigma)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    gratLap = cv.Laplacian(gray, ddepth, ksize=kernelSize, scale=scale, delta=delta)
    result = cv.convertScaleAbs(gratLap)
    
    return result
    
def sharpening(img, imgLaplacian):
    result = subtraction(img, imgLaplacian)
    return result

def unsharpMask(img):
    gaussian = cv.GaussianBlur(img, (11,11), 10)
    result = cv.addWeighted(img, 1.0+3.0, gaussian, -3.0, 0)
    return result

def highboost(img, boost_factor):
    gaussian = cv.GaussianBlur(img, (11,11), 10)
    result = cv.addWeighted(img, 1.0+3.0, gaussian, -3.0,  boost_factor)
    return result

def gradient(img):
    kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernelx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
    edges_x = cv.filter2D(img,cv.CV_8U,kernelx)
    edges_y = cv.filter2D(img,cv.CV_8U,kernely)
    
    return edges_x, edges_y

def roberts(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgLaplacian = laplacian(img)
    
    kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
    kernely = np.array([[0, -1], [1, 0]], dtype=int)
    x = cv.filter2D(grayImage, cv.CV_16S, kernelx)
    y = cv.filter2D(grayImage, cv.CV_16S, kernely)
    
    absX = cv.convertScaleAbs(x)
    absY = cv.convertScaleAbs(y)
    
    result = cv.addWeighted(absX, 0.5, absY, 0.5, 0)
    
    return result

def sobel(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    x = cv.Sobel(grayImage, cv.CV_16S, 1, 0)
    y = cv.Sobel(grayImage, cv.CV_16S, 0, 1)
    
    absX = cv.convertScaleAbs(x)
    absY = cv.convertScaleAbs(y)
    result = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

    return result