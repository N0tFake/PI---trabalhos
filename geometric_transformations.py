import cv2 as cv
import numpy as np

def translation(img, width, height):
    rows, columns = img.shape
    M = np.float32([[1,0,width],[0,1,height]])
    result = cv.warpAffine(img, M, (rows, columns))
    return result

def rotation(img, degree):
    rows, columns = img.shape
    M = cv.getRotationMatrix2D((columns/2, rows/2), degree, 1)
    result = cv.warpAffine(img, M, (columns, rows))
    return result

def scaling(img, x, y):
    height, width = img.shape[:2]
    result = cv.resize(img,(x*width, y*height), interpolation = cv.INTER_CUBIC)
    return result

def reflection(img, direction):
    result = cv.flip(img, direction)
    return result

