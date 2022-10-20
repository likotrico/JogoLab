import pygame
from pygame.locals import *
from sys import exit

def desenhaBloco(screen, colorblock, colorlineup, colorlinedown, inicio, blocklarg, blockalt):
    x0 = inicio[0]
    y0 = inicio[1]
    x_y0 = [x0, y0]
    list = []
    list.append(x_y0)

    pygame.draw.rect(screen, colorlineup, (list[0][0] + 1, list[0][1] + 1, blocklarg, blockalt))
    pygame.draw.rect(screen, colorlinedown, (list[0][0] + 4, list[0][1] + 4, blocklarg-3, blockalt-3))
    pygame.draw.rect(screen, colorblock, (list[0][0] + 4, list[0][1] + 4, blocklarg-6, blockalt-6))

def desenharTabuleiro8(screen):
    #tabuleiro 640x480
    x_inicial = 0
    y_inicial = 100
    newLarg = 80
    newAlt = 60

    for i in range(0, 8):
        for j in range(0,8):
            desenhaBloco(screen, cinza, branco, cinzaEscuro, (x_inicial+newLarg*j, y_inicial + newAlt * i), newLarg, newAlt)

def desenharTabuleiro16(screen):
    #tabuleiro 640x480
    x_inicial = 0
    y_inicial = 100
    newLarg = 40
    newAlt = 30
    for i in range(0, 16):
        for j in range(0,16):
            desenhaBloco(screen, cinza, branco, cinzaEscuro, (x_inicial+newLarg*j, y_inicial + newAlt * i), newLarg, newAlt)

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

    desenharTabuleiro16(tela)

    pygame.display.update()
