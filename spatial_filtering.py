from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import cv2 as cv

img = cv.imread('imagens/lena_noise.png', 0)

openCV = cv.medianBlur(img, 3)

def median_filter(img, filter_size):
    temp = []
    indexer = filter_size // 2;
    result = np.zeros(shape=(len(img), len(img[0])), dtype=np.uint8)
    for y in range(len(img)):
        for x in range(len(img[0])):
            for z in range(filter_size):
                if (y + z - indexer < 0) or (y + z - indexer > len(img)-1):
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if (x + z - indexer < 0) or (x + indexer > len(img[0])-1):
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(img[y + z - indexer][x + k - indexer])
            temp.sort()
            result[y][x] = temp[len(temp)// 2]
            temp = []
    return result


result = median_filter(img, 3)

fig = plt.figure(figsize=(8,4))
rows, columns = 1, 3

fig.add_subplot(rows, columns, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_RGB2BGR))
plt.axis('off')
plt.title('Original')

fig.add_subplot(rows, columns, 2)
plt.imshow(cv.cvtColor(openCV, cv.COLOR_RGB2BGR))
plt.axis('off')
plt.title('OpenCV')

fig.add_subplot(rows, columns, 3)
plt.imshow(cv.cvtColor(result, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Media')

plt.show()

 