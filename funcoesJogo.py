import pygame
from mecanica_celulas import obj
import time

azul = (0, 0, 255)
branco = (255, 255, 255)
cinza = (153, 153, 153)
cinzaEscuro = (102, 102, 102)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)


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
    elif type == 2:
        pygame.draw.rect(screen, branco, (coords[0], coords[1], larg, alt))
        pygame.draw.rect(screen, cinzaEscuro, (coords[0] + 4, coords[1] + 4, larg - 3, alt - 3))
        pygame.draw.rect(screen, azul, (coords[0] + 4, coords[1] + 4, larg - 6, alt - 6))

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
    if dimensoes == 16:
        for i in matriz:
            for j in i:
                if j.rect == coords:
                    screen.blit(texto, (((j.rect[0]) + (newlarg) / 2) - 3, ((j.rect[1]) + (newalt) / 4) - 3))

def rastreamento(matriz):
    print('entrou rast')
    print(len(matriz)-1)
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            count = 0
            if i - 1 >= 0 and j - 1 >=0:
                if matriz[i-1][j-1].bomb == 1:
                    count += 1
            if j - 1 >= 0:
                if matriz[i][j-1].bomb == 1:
                    count += 1
            if i + 1 <= len(matriz) - 1 and j - 1 >= 0:
                if matriz[i+1][j-1].bomb == 1:
                    count += 1
            if i - 1 >= 0:
                if matriz[i - 1][j].bomb == 1:
                    count += 1
            if i + 1 <= len(matriz)-1:
                if matriz[i+1][j].bomb == 1:
                    count += 1
            if i - 1 >= 0 and j + 1 <= len(matriz)-1:
                if matriz[i-1][j+1].bomb == 1:
                    count += 1
            if j+1<=len(matriz)-1:
                if matriz[i][j+1].bomb == 1:
                    count += 1
            if i+1<=len(matriz)-1 and j+1<=len(matriz)-1:
                if matriz[i+1][j+1].bomb == 1:
                    count += 1
            print(count)
            matriz[i][j].rast = count

def revelarAdjacentes(coords, matriz):
    verificacoes = []
    verificacoes.append(coords)
    verificados = []
    while len(verificacoes) != 0:
        x_coord = verificacoes[0][0]
        y_coord = verificacoes[0][1]
        print('verificacoes:')
        print(verificacoes)
        print('verificados')
        print(verificados)
        for X in range(0, len(matriz)):
            for Y in range(0, len(matriz)):
                if matriz[X][Y].rect == [x_coord, y_coord] and matriz[X][Y].rast == 0 and (matriz[X][Y].rect in verificados) == False:
                    if Y - 1 >= 0:
                        if matriz[X][Y - 1].bomb == 0 and (matriz[X][Y - 1].rect in verificados) == False:
                            matriz[X][Y - 1].cond = 1
                            verificacoes.append(matriz[X][Y - 1].rect)
                    if X - 1 >= 0:
                        if matriz[X - 1][Y].bomb == 0 and (matriz[X - 1][Y].rect in verificados) == False:
                            matriz[X - 1][Y].cond = 1
                            verificacoes.append(matriz[X - 1][Y].rect)
                    if X + 1 <= len(matriz) - 1:
                        if matriz[X + 1][Y].bomb == 0 and (matriz[X + 1][Y].rect in verificados) == False:
                            matriz[X + 1][Y].cond = 1
                            verificacoes.append(matriz[X + 1][Y].rect)
                    if Y + 1 <= len(matriz) - 1:
                        if matriz[X][Y + 1].bomb == 0 and (matriz[X][Y + 1].rect in verificados) == False:
                            matriz[X][Y + 1].cond = 1
                            verificacoes.append(matriz[X][Y + 1].rect)
                    if X - 1 >= 0 and Y - 1 >= 0:
                        if matriz[X-1][Y-1].bomb == 0 and (matriz[X-1][Y-1].rect in verificados) == False:
                            matriz[X-1][Y-1].cond = 1
                            verificacoes.append(matriz[X-1][Y-1].rect)
                    if X + 1 <= len(matriz) - 1 and Y - 1 >= 0:
                        if matriz[X+1][Y-1].bomb == 0 and (matriz[X+1][Y-1].rect in verificados) == False:
                            matriz[X + 1][Y - 1].cond = 1
                            verificacoes.append(matriz[X+1][Y-1].rect)
                    if X - 1 >= 0 and Y + 1 <= len(matriz) - 1:
                        if matriz[X-1][Y+1].bomb == 0 and (matriz[X-1][Y+1].rect in verificados) == False:
                            matriz[X - 1][Y + 1].cond = 1
                            verificacoes.append(matriz[X-1][Y+1].rect)
                    if X + 1 <= len(matriz) - 1 and Y + 1 <= len(matriz) - 1:
                        if matriz[X+1][Y+1].bomb == 0 and (matriz[X+1][Y+1].rect in verificados) == False:
                            matriz[X + 1][Y + 1].cond = 1
                            verificacoes.append(matriz[X+1][Y+1].rect)
        if len(verificacoes) > 0:
            verificados.append([x_coord, y_coord])
            verificacoes.remove([x_coord,y_coord])

def iniciarContagem():
    return time.time()

def atualizarContagem(tempo):
    return ((time.time())- tempo)