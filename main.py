from arithmetic_operations import sum
from arithmetic_operations import subtraction
from arithmetic_operations import multiplication
from arithmetic_operations import division
from arithmetic_operations import result

from geometric_transformations import translation
from geometric_transformations import rotation
from geometric_transformations import scaling
from geometric_transformations import reflection

from histograms import histograms
from histograms import normalizeHist
from histograms import equalizeHist
from histograms import contrastStreching

from spatial_filtering import MFrepublication
from spatial_filtering import MFzeros
from spatial_filtering import MFpaddingZeros
from spatial_filtering import MFconvolution

import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
    clear()
    print("+------------------------------------------------------+")
    print("|           UFT - Processamento de Imagens             |")
    print("|                                                      |")
    print("|                 Trabalho 01 e 02                     |")
    print("|                                                      |")
    print("| Alunos:  Amauri Melo Mendes Jr                       |")
    print("|          Jhonata B. Silva                            |")
    print("|          Marcos Antonio Costa Filho                  |")
    print("|          Silvio Otavio C. da Silva                   |")
    print("+------------------------------------------------------+")

    print("|           Escolha uma das opções abaixo              |")
    print("|           [1] Operações aritimetias                  |")
    print("|           [2] Transformações geométricas             |")
    print("|           [3] Histogramas                            |")
    print("|           [4] Filtragem espacial - Smoothing         |")
    print("|           [0] Sair                                   |")
    print("+------------------------------------------------------+")
    opc = int(input('Opção: '))
    
    if opc == 0:
        exit()
    elif opc == 1:
        opMenu()
    elif opc == 2:
        tgMenu()
    elif opc == 3:
        histMenu()
    elif opc == 4:
        filterMenu()
        
def opMenu():
    clear()
    print("+------------------------------------------------------+")
    print("|              Operações aritimeticas                  |")
    print("+------------------------------------------------------+")
    print("|           Informe o diretorio das imagens            |")
    print("|              Ex: imagens/imagem.png                  |")
    print("|     Obs: As imagens tem que ter o mesmo tamanho      |")
    print("+------------------------------------------------------+")
    pathImg1 = input('Diretorio da primeira imagem: ')
    pathImg2 = input('Diretorio da segunda imagem: ')
    print("+------------------------------------------------------+")
    print("|         Informe a operação a ser realizada           |")
    print("+------------------------------------------------------+")
    print('| [1] Adição                                           |')
    print('| [2] Subtração                                        |')
    print('| [3] Multiplicação                                    |')
    print('| [4] Divisão                                          |')
    print('| [0] Para retornar para o menu                        |')
    print("+------------------------------------------------------+")
    op = int(input('Operação: '))

    if op == 0:
        mainMenu()
    elif op == 1 or op == 2 or op == 3 or op == 4:
        img1 = cv.imread(pathImg1)
        img2 = cv.imread(pathImg2)
        resultado = result(img1, img2, op)
        alert()
        opMostraImg(img1, img2, resultado)

        save(resultado)

def tgMenu():
    clear()
    print("+------------------------------------------------------+")
    print("|             Transformações geometricas               |")
    print("+------------------------------------------------------+")
    print("|           Informe o diretorio da imagem             |")
    print("|              Ex: imagens/imagem.png                  |")
    print("+------------------------------------------------------+")
    pathImg = input('Diretorio da imagem: ')
    print("+------------------------------------------------------+")
    print("|               Informe a transformação                |")
    print("+------------------------------------------------------+")
    print('| [1] Translação                                       |')
    print('| [2] Rotação                                          |')
    print('| [3] Escala                                           |')
    print('| [4] Reflexão                                         |')
    print('| [0] Para retornar para o menu                        |')
    print("+------------------------------------------------------+")
    op = int(input('Operação: '))

    if op == 0:
        mainMenu()
    elif op == 1:
        clear()
        print("+------------------------------------------------------+")
        print("| Para a translação necessita da largura e altura      |")
        print("+------------------------------------------------------+")
        width = int(input("informe a largura: "))
        height = int(input("informe a altura: "))
        
        img = cv.imread(pathImg, 0)
        result = translation(img, width, height)
        alert()
        tgMostraImg(img, result)
        save(result)
        
    elif op == 2:
        clear()
        print("+------------------------------------------------------+")
        print("| Para a rotação necessita do grau                     |")
        print("+------------------------------------------------------+")
        degree = int(input("informe o grau: "))
        
        img = cv.imread(pathImg, 0)
        result = rotation(img, degree)
        alert()
        tgMostraImg(img, result)
        save(result)
        
    elif op == 3:
        clear()
        print("+------------------------------------------------------+")
        print("| Para a escala, necessita dos valores de X e Y        |")
        print("+------------------------------------------------------+")
        x = int(input("informe o x: "))
        y = int(input("informe o y: "))
        
        img = cv.imread(pathImg, 0)
        result = scaling(img, x, y)
        alert()
        tgMostraImg(img, result)
        save(result)
        
    elif op == 4:
        clear()
        print("+------------------------------------------------------+")
        print("| Para a reflexão, necessita saber a direção           |")
        print("| [1] Horizontal                                       |")
        print("| [0] Vertical                                       |")
        print("+------------------------------------------------------+")
        direction = int(input("informe a direção: "))
        
        img = cv.imread(pathImg, 0)
        result = reflection(img, direction)
        alert()
        tgMostraImg(img, result)
        save(result)

def histMenu():
    clear()
    print("+------------------------------------------------------+")
    print("|                    Histrogramas                      |")
    print("+------------------------------------------------------+")
    print("|           Informe o diretorio da imagem              |")
    print("|              Ex: imagens/imagem.png                  |")
    print("+------------------------------------------------------+")
    pathImg = input('Diretorio da imagem: ')
    print("+------------------------------------------------------+")
    print("|                 Informe o histrograma                |")
    print("+------------------------------------------------------+")
    print('| [1] Histrograma                                      |')
    print('| [2] Histograma Normalizado                           |')
    print('| [3] Histograma equalizado e Enhancement              |')
    print('| [4] Contrast Streching                               |')
    print('| [0] Para retornar para o menu                        |')
    print("+------------------------------------------------------+")
    op = int(input('Operação: '))
    img = cv.imread(pathImg)
    alert()
    if op == 0:
        mainMenu()
    elif op == 1:
      histograms(img)
    elif op == 2:
        normalizeHist(img)
    elif op == 3:
        equalizeHist(img)
    elif op == 4:
        contrastStreching(img) 
    mainMenu()
 
def filterMenu():   
    clear()
    print("+------------------------------------------------------+")
    print("|           Filtragem espacial - Smoothing             |")
    print("+------------------------------------------------------+")
    print("|           Informe o diretorio da imagem              |")
    print("|              Ex: imagens/imagem.png                  |")
    print("+------------------------------------------------------+")
    pathImg = input('Diretorio da imagem: ')
    print("+------------------------------------------------------+")
    print("|           Informe o tamanho da vizinhança            |")
    print("|  Obs: Quanto maior o numero, mais tempo irá demorar  |")
    print("+------------------------------------------------------+")
    filter_size = int(input("Tamanho da vizinhança: "));
    alert()
    img = cv.imread(pathImg, 0)
    result1 = MFrepublication(img, filter_size)
    result2 = MFzeros(img, filter_size)
    result3 = MFpaddingZeros(img, filter_size)
    result4 = MFconvolution(img, filter_size)
    stMostraImg(img, result1, result2, result3, result4)
    mainMenu()    

def stMostraImg(img, result1, result2, result3, result4):
    fig = plt.figure(figsize=(12,5))
    rows, columns = 1, 5

    fig.add_subplot(rows, columns, 1)
    plt.imshow(cv.cvtColor(img, cv.COLOR_RGB2BGR))
    plt.axis('off')
    plt.title('Original')

    fig.add_subplot(rows, columns, 2)
    plt.imshow(cv.cvtColor(result1, cv.COLOR_RGB2BGR))
    plt.axis('off')
    plt.title('Tipo de borda:\n Replicação dos pixels')

    fig.add_subplot(rows, columns, 3)
    plt.imshow(cv.cvtColor(result2, cv.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title('Tipo de borda:\n Atribuindo zeros')

    fig.add_subplot(rows, columns, 4)
    plt.imshow(cv.cvtColor(result3, cv.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title('Tipo de borda:\n Padding com zeros')

    fig.add_subplot(rows, columns, 5)
    plt.imshow(cv.cvtColor(result4, cv.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title('Tipo de borda:\n Convulação Periódica')

    plt.show()
    
def tgMostraImg(img, result):
    
    fig = plt.figure(figsize=(10, 7))
    rows, columns = 1, 2
    
    fig.add_subplot(rows, columns, 1)
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Imagem original")
    
    fig.add_subplot(rows, columns, 2)
    plt.imshow(cv.cvtColor(result, cv.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Resultado")
    
    plt.show()

def opMostraImg(img1, img2, result):
    fig = plt.figure(figsize=(10, 7))
    rows, columns = 1, 3
    
    fig.add_subplot(rows, columns, 1)
    plt.imshow(img1)
    plt.axis('off')
    plt.title("Imagem 1")
    
    fig.add_subplot(rows, columns, 2)
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Imagem 2")
    
    fig.add_subplot(rows, columns, 3)
    plt.imshow(result)
    plt.axis('off')
    plt.title("Resultado")
    
    plt.show()

def alert():
    clear()
    print("+------------------------------------------------------+")
    print("| Foi aberto uma janela com o resultado.               |")
    print("| Olhe a barra de tarefas e verifique os resultados    |")
    print("| para continuar(Basta fechar a janela)                |")
    print("+------------------------------------------------------+")

def save(result):
    clear()
    print("+------------------------------------------------------+")
    print("|      Informe o nome do arquivo para salvar           |")
    print("|               Não colocar espaços                    |")
    print("|    Você poderá conferi-la na pasta 'resultado'       |")
    print("|    Ex: imgResult                                     |")
    print("+------------------------------------------------------+")
    name = input("Nome da imagem: ")
    file = name + '.png'
    path = 'resultados/' + file
    cv.imwrite(path, result)
    print("+------------------------------------------------------+")
    print("|                  Imagem salva                        |")
    print("+------------------------------------------------------+")
    print("+------------------------------------------------------+")
    print("|                Voltar para o menu?                   |")
    print("|                    [1] Sim                           |")
    print("|                    [0] Não(Sair)                     |")
    print("+------------------------------------------------------+")
    opc = int(input("Opção: "))
    
    if opc == 0:
        exit()
    else:
        mainMenu()
        
# MAIN        
mainMenu()
    
    
