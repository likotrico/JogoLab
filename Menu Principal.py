import pygame, sys
from pygame.locals import *


pygame.init()

largura = 640
altura = 580
azul = (65, 105, 225)
branco = (255, 255, 255)
preto = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
menu = True
instrucoes = True

fonte1 = pygame.font.SysFont('arial', 15, True, True)
fonte2 = pygame.font.SysFont('arial', 40, True, True)

BG1 = pygame.image.load('Menu screen/background1.png')
BG2 = pygame.image.load('Menu screen/background2.png')

while menu:
    msg_jogar = 'JOGAR'
    msg_instrucoes = 'INSTRUÇÕES'
    msg_sair = 'SAIR'

    texto_jogar = fonte2.render(msg_jogar, True, preto)
    texto_sair = fonte2.render(msg_sair, True, preto)
    texto_instrucoes = fonte2.render(msg_instrucoes, True, preto)

    rect_jogar = pygame.draw.rect(tela, preto, (240, 395, 160, 60))
    pygame.draw.rect(tela, preto, (245, 400, 150, 50))

    rect_instrucoes = pygame.draw.rect(tela, preto, (200, 455, 280, 60))
    pygame.draw.rect(tela, preto, (205, 460, 270, 50))

    rect_sair = pygame.draw.rect(tela, preto, (268, 510, 100, 60))
    pygame.draw.rect(tela, preto, (273, 515, 110, 50))

    tela.blit(BG1, (0, 0))
    tela.blit(texto_jogar, (245, 400))
    tela.blit(texto_instrucoes, (205, 460))
    tela.blit(texto_sair, (273, 515))

    coordrato = pygame.mouse.get_pos()
    rato = pygame.draw.rect(tela, (0, 0, 0), (coordrato[0], coordrato[1], 1, 1))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if rato.colliderect(rect_jogar):
            texto_jogar = fonte2.render(msg_jogar, True, branco)
            tela.blit(texto_jogar, (245, 400))

        if rato.colliderect(rect_instrucoes):
            texto_instrucoes = fonte2.render(msg_instrucoes, True, branco)
            tela.blit(texto_instrucoes, (205, 460))

        if rato.colliderect(rect_sair):
            texto_sair = fonte2.render(msg_sair, True, branco)
            tela.blit(texto_sair, (273, 515))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if rect_jogar.colliderect(rato):
                    modo = True
                    while modo:
                        msg_facil = 'FÁCIL'
                        msg_dificil = 'DIFÍCIL'
                        msg_voltar = 'VOLTAR'

                        texto_voltar = fonte2.render(msg_voltar, True, preto)
                        texto_facil = fonte2.render(msg_facil, True, preto)
                        texto_dificil = fonte2.render(msg_dificil, True, preto)

                        rect_voltar = pygame.draw.rect(tela, preto, (245, 510, 160, 60))
                        pygame.draw.rect(tela, preto, (250, 515, 150, 50))
                        rect_facil = pygame.draw.rect(tela, preto, (255, 195, 160, 60))
                        pygame.draw.rect(tela, preto, (260, 200, 150, 50))
                        rect_dificil = pygame.draw.rect(tela, preto, (245, 265, 160, 60))
                        pygame.draw.rect(tela, preto, (250, 270, 150, 50))

                        tela.blit(BG2, (0, 0))
                        tela.blit(texto_facil, (260, 200))
                        tela.blit(texto_dificil, (250, 270))
                        tela.blit(texto_voltar, (250, 515))
                        coordrato = pygame.mouse.get_pos()
                        rato = pygame.draw.rect(tela, (0, 0, 0), (coordrato[0], coordrato[1], 1, 1))
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                exit()

                            if rato.colliderect(rect_facil):
                                texto_facil = fonte2.render(msg_facil, True, branco)
                                tela.blit(texto_facil, (260, 200))

                            if rato.colliderect(rect_dificil):
                                texto_dificil = fonte2.render(msg_dificil, True, branco)
                                tela.blit(texto_dificil, (250, 270))

                            if rato.colliderect(rect_voltar):
                                texto_voltar = fonte2.render(msg_voltar, True, branco)
                                tela.blit(texto_voltar, (250, 515))

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                    if rect_facil.colliderect(rato):
                                        print('Modo fácil')
                                    elif rect_dificil.colliderect(rato):
                                        print('Modo difícil')
                                    elif rect_voltar.colliderect(rato):
                                        modo = False
                        pygame.display.flip()
                elif rect_sair.colliderect(rato):
                    print('Adeus')
                    menu = False
                elif rect_instrucoes.colliderect(rato):
                    instrucoes = True
                    while instrucoes:
                        msg_voltar = 'VOLTAR'

                        texto_voltar = fonte2.render(msg_voltar, True, preto)

                        rect_voltar = pygame.draw.rect(tela, preto, (245, 510, 160, 60))
                        pygame.draw.rect(tela, preto, (250, 515, 150, 50))

                        tela.blit(BG2, (0, 0))
                        tela.blit(texto_voltar, (250, 515))

                        coordrato = pygame.mouse.get_pos()
                        rato = pygame.draw.rect(tela, (0, 0, 0), (coordrato[0], coordrato[1], 1, 1))
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                exit()
                        if rato.colliderect(rect_voltar):
                            texto_voltar = fonte2.render(msg_voltar, True, branco)
                            tela.blit(texto_voltar, (250, 515))

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                if rect_voltar.colliderect(rato):
                                    instrucoes = False

                        pygame.display.flip()

        pygame.display.flip()














