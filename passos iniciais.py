import pygame
from mecanica_celulas import obj
from pygame.locals import *
from sys import exit

def gerarMatriz(num):
    matriz = []
    aux = []
    for i in range(0, num):
        for j in range(0, num):
            objaux = obj([i, j], 0, 0, 0)
            aux.append(objaux)
        matriz.append(aux)
        aux = []
    return matriz

def printMatriz(matriz, screen, larg, alt, num):
    Lista = matriz
    y_inicial = 100
    newLarg = (larg) / num
    newAlt = (alt - y_inicial) / num
    for lista in Lista:
        for cell in lista:
            printarBlock(screen, cell.rect, newLarg, newAlt, cell.cond)

def printarBlock(screen, coords, larg, alt, type):
    branco = (255, 255, 255)
    cinza = (153, 153, 153)
    cinzaEscuro = (102, 102, 102)
    preto = (0, 0, 0)
    vermelho = (255, 0, 0)
    if type == 0:
        pygame.draw.rect(screen, branco, (coords[0], coords[1], larg, alt))
        pygame.draw.rect(screen, cinzaEscuro, (coords[0] + 4, coords[1] + 4, larg - 3, alt - 3))
        pygame.draw.rect(screen, cinza, (coords[0] + 4, coords[1] + 4, larg - 6, alt - 6))
    elif type == 1:
        pygame.draw.rect(screen, branco, (coords[0], coords[1], larg, alt))
        pygame.draw.rect(screen, cinzaEscuro, (coords[0] + 4, coords[1] + 4, larg - 3, alt - 3))
        pygame.draw.rect(screen, vermelho, (coords[0] + 4, coords[1] + 4, larg - 6, alt - 6))


def gerarTabuleiro(matriz, larg, alt, num):
    x_inicial = 0
    y_inicial = 100
    newLarg = (larg) / num
    newAlt = (alt - y_inicial) / num
    for i in range(0, num):
        for j in range(0, num):
            matriz[i][j].rect = [x_inicial + newLarg * j, y_inicial + newAlt * i]

def Tabuleiro(screen, larg, alt, num):
    matriz = gerarMatriz(num)
    x_inicial = 0
    y_inicial = 100
    newLarg = (larg)/num
    newAlt = (alt-y_inicial)/num
    for i in range(0, num):
         for j in range(0, num):
            matriz[i][j].rect = [x_inicial + newLarg * j, y_inicial + newAlt * i]

    matriz[0][0].cond = 1
    for lista in matriz:
        for cell in lista:
            printarBlock(screen, cell.rect, newLarg, newAlt, cell.cond)


pygame.init()

largura = 640 # Largura da Tela
altura = 580 # Altura da Tela


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Teste pygame') # Nome da Janela do jogo

dimensoes = 8 # Dimensão que pode ser alterada
matriz = gerarMatriz(dimensoes) #Matriz que vai armadezar todas as informações de uma dada célula
gerarTabuleiro(matriz, largura, altura, dimensoes) #Alterar a matriz com todas as informações necessárias

newLarg = (largura) / dimensoes # Largura das Células
newAlt = (altura - 100) / dimensoes # Altura das Células

objetos = [] #Lista dos objetos que serão utilizados para colisões

# For que gera os objetos para colisão e os coloca na lista de objetos
for i in matriz:
    for j in i:
        xy = j.rect
        obj_aux = pygame.draw.rect(tela, (0,0,0), (xy[0], xy[1], newLarg, newAlt))
        objetos.append(obj_aux)
    obj_aux = []

while True:

    printMatriz(matriz, tela, largura, altura, dimensoes)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(coordrato)
            for i in objetos:
                if i.colliderect(rato):
                    for algo in matriz:
                        for outro in algo:
                            vetor = [i[0], i[1]]
                            if vetor == outro.rect:
                                if outro.cond == 1:
                                    outro.cond = 0
                                elif outro.cond == 0:
                                    outro.cond = 1



    #Informações da localização do mouse
    coordrato = pygame.mouse.get_pos()
    rato = pygame.draw.rect(tela, (0, 0, 0), (coordrato[0], coordrato[1], 1, 1))

    pygame.display.update()
