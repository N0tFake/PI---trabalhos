import cv2 as cv
import numpy as np

img = cv.imread('imagens/lena200.png', 0)

def tramslation(width, height):
    rows, columns = img.shape
    M = np.float32([[1,0,width],[0,1,height]])
    result = cv.warpAffine(img, M, (rows, columns))
    return result

def rotation():
    rows, columns = img.shape
    M = cv.getRotationMatrix2D((columns/2, rows/2), 90, 1)
    result = cv.warpAffine(img, M, (columns, rows))
    return result



result = rotation()
cv.imshow('teste', result)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows() 