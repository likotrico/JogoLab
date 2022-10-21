import pygame
from random import randint
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

def printarNumero(matriz, screen, newlarg, newalt, texto, coords, dimensoes):
    if dimensoes == 8:
        for i in matriz:
            for j in i:
                if j.rect == coords:
                    screen.blit(texto, (((j.rect[0])+(newlarg)/2)-7, ((j.rect[1])+(newalt)/4)-7))

def rastreamento(matriz, newLarg, newAlt, largura, altura, x_inicial, y_inicial):
    print('entrou rast')
    print(len(matriz)-1)
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            count = 0
            if i - 1 >= 0 and j - 1 >=0:
                if matriz[i-1][j-1].bomb == 1:
                    count += 1
                    print('entrou')
            if j - 1 >= 0:
                if matriz[i][j-1].bomb == 1:
                    count += 1
                    print('entrou')
            if i + 1 <= len(matriz) - 1 and j - 1 >= 0:
                if matriz[i+1][j-1].bomb == 1:
                    count += 1
                    print('entrou')
            if i - 1 >= 0:
                if matriz[i - 1][j].bomb == 1:
                    count += 1
                    print('entrou')
            if i + 1 <= len(matriz)-1:
                if matriz[i+1][j].bomb == 1:
                    count += 1
                    print('entrou')
            if i - 1 >= 0 and j + 1 <= len(matriz)-1:
                if matriz[i-1][j+1].bomb == 1:
                    count += 1
                    print('entrou')
            if j+1<=len(matriz)-1:
                if matriz[i][j+1].bomb == 1:
                    count += 1
                    print('entrou')
            if i+1<=len(matriz)-1 and j+1<=len(matriz)-1:
                if matriz[i+1][j+1].bomb == 1:
                    count += 1
                    print('entrou')
                print(count)
                matriz[i][j].rast = count


pygame.init()

largura = 640 # Largura da Tela
altura = 580 # Altura da Tela

#Cores
azul = (0, 0, 255)
branco = (255, 255, 255)
cinza = (153, 153, 153)
cinzaEscuro = (102, 102, 102)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Teste pygame') # Nome da Janela do jogo

dimensoes = 8 # Dimensão que pode ser alterada
qtd_bombas = dimensoes + 1
#Organizando fonte
tamanho_fonte = 0
if dimensoes == 8:
    tamanho_fonte = 40
else:
    tamanho_fonte = 10

fonte = pygame.font.SysFont('arial', tamanho_fonte, False, False)

matriz = gerarMatriz(dimensoes) #Matriz que vai armadezar todas as informações de uma dada célula
gerarTabuleiro(matriz, largura, altura, dimensoes) #Alterar a matriz com todas as informações necessárias

newLarg = int((largura) / dimensoes) # Largura das Células
newAlt = int((altura - 100) / dimensoes) # Altura das Células



objetos = [] #Lista dos objetos que serão utilizados para colisões

# For que gera os objetos para colisão e os coloca na lista de objetos
for i in matriz:
    for j in i:
        xy = j.rect
        obj_aux = pygame.draw.rect(tela, (0,0,0), (xy[0], xy[1], newLarg, newAlt))
        objetos.append(obj_aux)
    obj_aux = []



qtd_reveladas = 0

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

    #IMPRIMIR AS MINAS DETECTADAS NAS CÉLULAS REVELADAS
    for numero in matriz:
        for elemento in numero:
            informação_mina_detectada = f'{elemento.rast}'
            texto_mina_detectada = fonte.render(informação_mina_detectada, True, azul)
            informação_bomba = f'{elemento.bomb}'
            texto_bomba = fonte.render(informação_bomba, True, verde)
            if elemento.cond == 1:
                printarNumero(matriz, tela, newLarg, newAlt, texto_bomba, elemento.rect, dimensoes)
                printarNumero(matriz, tela, newLarg, newAlt, texto_mina_detectada, elemento.rect, dimensoes)
                qtd_reveladas += 1

    #Condição para que a primeira casa revelada não contenha bomba
    if qtd_reveladas == 1:
        print('first play')
        # Preenchendo a matriz com as bombas
        while qtd_bombas != 0:
            x_random = randint(0, dimensoes - 1)
            y_random = randint(0, dimensoes - 1)
            if matriz[x_random][y_random].bomb == 0 and matriz[x_random][y_random].cond != 1:
                matriz[x_random][y_random].bomb = 1
                qtd_bombas = qtd_bombas - 1
        rastreamento(matriz, newLarg, newAlt, largura, altura, 0, 100)
        print('ok')
        first_play = False

    pygame.display.update()
