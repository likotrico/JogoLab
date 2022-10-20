import pygame
from pygame.locals import *
from sys import exit

def desenhaBloco(screen, colorblock, colorlineup, colorlinedown, inicio, fim, blocklarg, blockalt):
    x0 = inicio[0]
    y0 = inicio[1]
    x_y0 = [x0, y0]
    x = fim[0]
    y = fim[1]-1
    x_y = [x, y]
    list = []
    list.append(x_y0)
    list2 = []
    list2.append(x_y)

    #QUADRADO CINZA
    pygame.draw.rect(screen, colorblock, (0, 100, blocklarg, blockalt))

    #LINHAS BRANCAS DE CIMA
    for i in range(0,3):
        pygame.draw.line(screen, colorlineup, list[0], list2[0])
        list[0][0] = list[0][0] + 1
        list2[0][0] = list2[0][0] + 1
    list[0][0] = x0 - 1
    list2[0][0] = x - 1
    list[0][1] = list[0][1] - 1 #CORREÇÃO DE UM PROBLEMA DE SIMETRIA
    list2[0][0] = list2[0][0] + blocklarg
    list2[0][1] = list2[0][1] - blockalt
    for i in range(0,3):
        print(list)
        print(list2)
        pygame.draw.line(screen, colorlineup, list[0], list2[0])
        list[0][1] = list[0][1] + 1
        list2[0][1] = list2[0][1] + 1

    list[0][1] = y0 - 1
    list2[0][1] = y
    list[0][1] = list[0][1] + blockalt
    for i in range(0, 3):
        pygame.draw.line(screen, colorlinedown, list[0], list2[0])
        list[0][1] = list[0][1] - 1
        list2[0][1] = list2[0][1] - 1
    list[0][1] = y0 - 1
    list2[0][1] = y
    list[0][0] = list[0][0] + blocklarg

    for i in range(0, 3):
        pygame.draw.line(screen, colorlinedown, list[0], list2[0])
        list[0][0] = list[0][0] - 1
        list2[0][0] = list2[0][0] - 1




def desenhaBloco2(screen, colorblock, colorlineup, colorlinedown, inicio, fim, blocklarg, blockalt):
    x0 = inicio[0]
    y0 = inicio[1]
    x_y0 = [x0, y0]
    list = []
    list.append(x_y0)

    pygame.draw.rect(screen, colorlineup, (list[0][0] + 1, list[0][1] + 1, blocklarg, blockalt))
    pygame.draw.rect(screen, colorlinedown, (list[0][0] + 4, list[0][1] + 4, blocklarg-3, blockalt-3))
    pygame.draw.rect(screen, colorblock, (list[0][0] + 4, list[0][1] + 4, blocklarg-6, blockalt-6))




def desenharTabuleiro8(largTela, altTela, screen):
    #tabuleiro 640x480
    x_inicial = 0
    y_inicial = 100
    newLarg = 80
    newAlt = 60
    #desenhaBloco2(screen, cinza, branco, cinzaEscuro, (x_inicial, y_inicial), (x_inicial,y_inicial+newAlt), newLarg, newAlt)

    #pygame.draw.rect(screen, branco, (x_inicial + newLarg + 1, y_inicial + newAlt + 1, newLarg, newAlt))
    #pygame.draw.rect(screen, cinzaEscuro, (x_inicial+newLarg+4, y_inicial+newAlt+4, newLarg-3, newAlt-3))
    #pygame.draw.rect(screen, cinza, (x_inicial+newLarg+4, y_inicial+newAlt+4, newLarg-6, newAlt-6))
    aux = 0
    for i in range(0, 8):
        #desenhaBloco2(screen, cinza, branco, cinzaEscuro,(x_inicial, y_inicial+newAlt*i) ,(x_inicial, y_inicial+i) ,newLarg, newAlt)
        pygame.draw.line(tela, vermelho, (x_inicial, y_inicial), (x_inicial, y_inicial + newAlt))
        for j in range(0,8):
            desenhaBloco2(screen, cinza, branco, cinzaEscuro, (x_inicial+newLarg*j, y_inicial + newAlt * i),(x_inicial, y_inicial + i), newLarg, newAlt)

    #pygame.draw.line(screen, branco, (0,200), (0,201))
    #for i in range(100, altTela, newAlt):
        #pygame.draw.line(screen, vermelho, (0, i), (largTela, i))
    #for j in range(0, largTela, newLarg):
        #pygame.draw.line(screen, vermelho, (j,100), (j, altTela))



pygame.init()

largura = 640
altura = 580
cinza = (153, 153, 153)
cinzaEscuro = (102, 102, 102)
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Teste pygame')


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #pygame.draw.rect(tela, cinza, (0, 100, 80, 60))


#    pygame.draw.line(tela, branco, (largura / 2, altura / 2), ((largura / 2), (altura / 2) + 39))
#    pygame.draw.line(tela, branco, ((largura / 2) + 1, altura / 2), ((largura / 2) + 1, (altura / 2) + 39))
#    pygame.draw.line(tela, branco, ((largura / 2) + 2, altura / 2), ((largura / 2) + 2, (altura / 2) + 39))
#    pygame.draw.line(tela, branco, (largura / 2, altura / 2), ((largura / 2) + 39, (altura / 2)))
#    pygame.draw.line(tela, branco, (largura / 2, (altura / 2) + 1), ((largura / 2) + 39, (altura / 2) + 1))
#    pygame.draw.line(tela, branco, (largura / 2, (altura / 2) + 2), ((largura / 2) + 39, (altura / 2) + 2))

#    pygame.draw.line(tela, cinzaEscuro, (largura / 2, (altura / 2) + 39), ((largura / 2) + 39, (altura / 2) + 39))
#    pygame.draw.line(tela, cinzaEscuro, (largura / 2, (altura / 2) + 38), ((largura / 2) + 39, (altura / 2) + 38))
#    pygame.draw.line(tela, cinzaEscuro, (largura / 2, (altura / 2) + 37), ((largura / 2) + 39, (altura / 2) + 37))
#    pygame.draw.line(tela, cinzaEscuro, ((largura / 2) + 39, (altura / 2)), ((largura / 2) + 39, (altura / 2) + 39))
#    pygame.draw.line(tela, cinzaEscuro, ((largura / 2) + 38, (altura / 2)), ((largura / 2) + 38, (altura / 2) + 39))
#    pygame.draw.line(tela, cinzaEscuro, ((largura / 2) + 37, (altura / 2)), ((largura / 2) + 37, (altura / 2) + 39))

    desenharTabuleiro8(largura, altura, tela)





    pygame.display.update()
