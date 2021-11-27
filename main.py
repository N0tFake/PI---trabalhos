from arithmetic_operations import sum
from arithmetic_operations import subtraction
from arithmetic_operations import multiplication
from arithmetic_operations import division
from arithmetic_operations import result

import os
import cv2 as cv

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
    print('| [0] Multiplicação                                    |')
    print('| [0] Divisão                                          |')
    print('| [0] Para retornar para o menu                        |')
    print("+------------------------------------------------------+")
    op = int(input('Operação: '))

    if op == 0:
        mainMenu()
    elif op == 1 or op == 2 or op == 3 or op == 4:
        img1 = cv.imread(pathImg1)
        img2 = cv.imread(pathImg2)
        resultado = result(img1, img2, op)
        print("+------------------------------------------------------+")
        print("|      Informe o nome do arquivo para salvar           |")
        print("|               Não colocar espaços                    |")
        print("|    Você poderá conferi-la na pasta 'resultado'       |")
        print("|    Ex: imgResult                                     |")
        print("+------------------------------------------------------+")
        name = input("Nome da imagem: ")
        save(name, resultado)

def save(name, result):
    clear()
    file = name + '.png'
    path = 'resultado/' + file
    cv.imwrite(path, result)
    print("+------------------------------------------------------+")
    print("|                  Imagem salva                        |")
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
    
    
