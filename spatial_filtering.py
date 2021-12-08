from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import cv2 as cv

img = cv.imread('imagens/tree.png', 0)

openCV = cv.medianBlur(img, 3)

#  Replicação dos pixels das bordas
def MFrepublication(img, filter_size):
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
    for y in range(len(img)):
        for x in range(len(img[0])):
            if (x == 0) or (x == len(img)-1) or (y == 0) or (x == len(img[0])-1):
                result[y][x] = img[y][x]
    
    return result

# Atribuindo zero aos resultados não calculáveis
def MFzeros(img, filter_size):
    temp = []
    indexer = filter_size // 2;
    result = np.zeros(shape=(len(img), len(img[0])), dtype=np.uint8)
    for y in range(len(img)):
        for x in range(len(img[0])):
            for z in range(filter_size):
                if (y + z - indexer <= 1) or (y + z - indexer >= len(img)-1):
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if (x + z - indexer <= 1) or (x + indexer >= len(img[0])-1):
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(img[y + z - indexer][x + k - indexer])
            temp.sort()
            result[y][x] = temp[len(temp)// 2]
            temp = []
    return result

# Padding com zeros
def MFpaddingZeros(img, filter_size):
    temp = []
    indexer = filter_size // 2;
    result = np.zeros(shape=(len(img), len(img[0])), dtype=np.uint8)
    for y in range(len(img)):
        for x in range(len(img[0])):
            for z in range(filter_size):
                if (y + z - indexer <= 0) or (y + z - indexer >= len(img)-1):
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if (x + z - indexer <= 0) or (x + indexer >= len(img[0])-1):
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(img[y + z - indexer][x + k - indexer])
            temp.sort()
            result[y][x] = temp[len(temp)// 2]
            temp = []
    return result

#  Convolução Periódica
def MFconvolution(img, filter_size):
    temp = []
    indexer = filter_size // 2;
    result = np.zeros(shape=(len(img), len(img[0])), dtype=np.uint8)
    for y in range(len(img)):
        for x in range(len(img[0])):
            for z in range(filter_size):
                if (y + z - indexer <= 0) or (y + z - indexer >= len(img)-1):
                    for c in range(filter_size):
                        temp.append(img[y][len(img[0])-1])
                else:
                    if (x + z - indexer <= 0) or (x + indexer >= len(img[0])-1):
                        temp.append(img[y][len(img[0])-1])
                    else:
                        for k in range(filter_size):
                            temp.append(img[y + z - indexer][x + k - indexer])
            temp.sort()
            result[y][x] = temp[len(temp)// 2]
            temp = []
    return result

result1 = MFrepublication(img, 3)
result2 = MFzeros(img, 3)
result3 = MFpaddingZeros(img, 3)
result4 = MFconvolution(img, 3)

fig = plt.figure(figsize=(10,5))
rows, columns = 1, 5

fig.add_subplot(rows, columns, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_RGB2BGR))
plt.axis('off')
plt.title('Original')

fig.add_subplot(rows, columns, 2)
plt.imshow(cv.cvtColor(result1, cv.COLOR_RGB2BGR))
plt.axis('off')
plt.title('MF replicação')

fig.add_subplot(rows, columns, 3)
plt.imshow(cv.cvtColor(result2, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.title('MF zeros')

fig.add_subplot(rows, columns, 4)
plt.imshow(cv.cvtColor(result3, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.title('MF padding')

fig.add_subplot(rows, columns, 5)
plt.imshow(cv.cvtColor(result4, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.title('MF convulação')

plt.show()

 