from arithmetic_operations import sum
from arithmetic_operations import subtraction
from arithmetic_operations import multiplication
from arithmetic_operations import division
from arithmetic_operations import result

from geometric_transformations import translation
from geometric_transformations import rotation
from geometric_transformations import scaling
from geometric_transformations import reflection

import os
import cv2 as cv
import numpy as np

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
    print("|           [0] Sair                                   |")
    print("+------------------------------------------------------+")
    opc = int(input('Opção: '))
    
    if opc == 0:
        exit()
    elif opc == 1:
        opMenu()
    elif opc == 2:
        tgMenu()
        
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
        imgs = np.concatenate((img1, img2, resultado), axis=1)
        cv.imshow('Resultado', imgs)
        cv.waitKey(0)

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
        seta = cv.imread('operadores/seta.png', 0)
        imgs = np.concatenate((img, seta, result), axis=1)
        alert()
        cv.imshow('Resultado', imgs)
        cv.waitKey(0)
        save(result)
        
    elif op == 2:
        clear()
        print("+------------------------------------------------------+")
        print("| Para a rotação necessita do grau                     |")
        print("+------------------------------------------------------+")
        degree = int(input("informe o grau: "))
        
        img = cv.imread(pathImg, 0)
        result = rotation(img, degree)
        seta = cv.imread('operadores/seta.png', 0)
        imgs = np.concatenate((img, seta, result), axis=1)
        alert()
        cv.imshow('Resultado', imgs)
        cv.waitKey(0)
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
        seta = cv.imread('operadores/seta.png', 0)
        imgs = np.concatenate((img, seta, result), axis=1)
        alert()
        cv.imshow('Resultado', imgs)
        cv.waitKey(0)
        save(result)

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
    path = 'resultado/' + file
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
    
    
