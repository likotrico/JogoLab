import pygame
from pygame.locals import *
from sys import exit
from math import floor
from time import sleep

pygame.init()

#largura = 640
#altura = 580


#tela = pygame.display.set_mode((largura, altura))
#pygame.display.set_caption('Sprites')


class Bomberman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(0, 4):
            self.sprites.append(pygame.image.load('Sprites/walking-right1.png'))
            self.sprites.append(pygame.image.load('Sprites/walking-right2.png'))
            self.sprites.append(pygame.image.load('Sprites/walking-right3.png'))

        self.sprites.append(pygame.image.load('Sprites/front-left.png'))
        self.sprites.append(pygame.image.load('Sprites/front.png'))
        self.sprites.append(pygame.image.load('Sprites/front2.png'))
        self.sprites.append(pygame.image.load('Sprites/front3.png'))
        self.sprites.append(pygame.image.load('Sprites/front3.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 250
        self.rect.midleft = self.x, self.y



    def update(self, tela):
        self.atual += 0.15
        if self.atual <= len(self.sprites):
            self.image = self.sprites[floor(self.atual)]
            self.image = pygame.transform.scale(self.image, (22 * 3, 25 * 3))
            if self.atual < 11:
                self.x += 3.75
                self.rect.midleft = self.x, self.y
        else:
            sleep(0.5)
            self.sprites.clear()





def rodarAnimacaoInicial(screen):
    tela = screen

    AZUL = (65, 105, 225)
    todas_as_sprites = pygame.sprite.Group()
    bomberman = Bomberman()
    todas_as_sprites.add(bomberman)
    img = pygame.image.load('Sprites/CampoMinado.png')


    relogio = pygame.time.Clock()
    animacao = True
    while animacao:
        relogio.tick(30)
        tela.fill(AZUL)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    animacao = False
        todas_as_sprites.draw(tela)
        todas_as_sprites.update(tela)
        pygame.display.flip()

