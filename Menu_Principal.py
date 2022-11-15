import pygame, sys
from pygame.locals import *


pygame.init()

largura = 640
altura = 580
azul = (65, 105, 225)
branco = (255, 255, 255)
preto = (0, 0, 0)

#tela = pygame.display.set_mode((largura, altura))

def rodarMenu(screen):

    menu = True
    instrucoes = True

    tela = screen

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

        rect_sair = pygame.draw.rect(tela, preto, (268, 515, 100, 60))
        pygame.draw.rect(tela, preto, (273, 520, 110, 50))

        tela.blit(BG1, (0, 0))
        tela.blit(texto_jogar, (245, 400))
        tela.blit(texto_instrucoes, (205, 460))
        tela.blit(texto_sair, (273, 520))

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
                tela.blit(texto_sair, (273, 520))

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

                                pygame.display.flip()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                        if rect_facil.colliderect(rato):
                                            print('Modo fácil')
                                            return 8
                                        elif rect_dificil.colliderect(rato):
                                            print('Modo difícil')
                                            return 16
                                        elif rect_voltar.colliderect(rato):
                                            modo = False

                    elif rect_sair.colliderect(rato):
                        print('Adeus')
                        menu = False
                        return 0
                    elif rect_instrucoes.colliderect(rato):
                        instrucoes = True
                        while instrucoes:
                            msg_voltar = 'VOLTAR'
                            msg_ajuda1 = 'BOTÃO DIREITO DO MOUSE: marca a célula com uma bandeira (célula de cor azul) ou '
                            msg_ajuda11 = 'remove a marcação caso esteja marcada.'
                            msg_ajuda2 = 'COMO JOGAR: O objetivo do jogo é revelar todas as células que não possuem bombas'
                            msg_ajuda21 = 'no menor tempo possível. Ao revelar uma célula, ela possuirá um número indicando'
                            msg_ajuda22 = 'a quantidade de bombas nas células adjacentes. Se a célula revelada não possuir'
                            msg_ajuda23 = 'bombas ao redor, as células adjacentes serão reveladas automaticamente. Revelar'
                            msg_ajuda24 = 'uma célula com bomba resulta na derrota. A quantidade de bombas presente no campo'
                            msg_ajuda25 = 'é numericamente igual a quantidade de bandeiras disponíveis no inicio do jogo. A quan-'
                            msg_ajuda26 = 'tidade de bandeiras disponíveis no inicio do jogo. A bandeira serve para marcar uma cé-'
                            msg_ajuda27 = 'lula que o jogador acredita haver uma bomba. Uma célula marcada não pode ser revela-'
                            msg_ajuda28 = 'da. Ao marcar uma célula, uma bandeira é consumida. Caso seja desmarcada, a bandei-'
                            msg_ajuda29 = 'ra é recuperada.'
                            msg_ajuda3 = 'BOTÃO ESQUERDO DO MOUSE: revela a célula selecionada.'

                            texto_voltar = fonte2.render(msg_voltar, True, preto)
                            texto_ajuda1 = fonte1.render(msg_ajuda1, True, branco)
                            texto_ajuda11 = fonte1.render(msg_ajuda11, True, branco)
                            texto_ajuda2 = fonte1.render(msg_ajuda2, True, branco)
                            texto_ajuda21 = fonte1.render(msg_ajuda21, True, branco)
                            texto_ajuda22 = fonte1.render(msg_ajuda22, True, branco)
                            texto_ajuda23 = fonte1.render(msg_ajuda23, True, branco)
                            texto_ajuda24 = fonte1.render(msg_ajuda24, True, branco)
                            texto_ajuda25 = fonte1.render(msg_ajuda25, True, branco)
                            texto_ajuda26 = fonte1.render(msg_ajuda26, True, branco)
                            texto_ajuda27 = fonte1.render(msg_ajuda27, True, branco)
                            texto_ajuda28 = fonte1.render(msg_ajuda28, True, branco)
                            texto_ajuda29 = fonte1.render(msg_ajuda29, True, branco)
                            texto_ajuda3 = fonte1.render(msg_ajuda3, True, branco)

                            rect_voltar = pygame.draw.rect(tela, preto, (245, 510, 160, 60))
                            pygame.draw.rect(tela, preto, (250, 515, 150, 50))

                            tela.blit(BG2, (0, 0))
                            tela.blit(texto_voltar, (250, 515))
                            tela.blit(texto_ajuda1, (20, 20))
                            tela.blit(texto_ajuda11, (20, 40))
                            tela.blit(texto_ajuda2, (20, 80))
                            tela.blit(texto_ajuda21, (20, 100))
                            tela.blit(texto_ajuda22, (20, 120))
                            tela.blit(texto_ajuda23, (20, 140))
                            tela.blit(texto_ajuda24, (20, 160))
                            tela.blit(texto_ajuda25, (20, 180))
                            tela.blit(texto_ajuda26, (20, 200))
                            tela.blit(texto_ajuda27, (20, 220))
                            tela.blit(texto_ajuda28, (20, 240))
                            tela.blit(texto_ajuda29, (20, 260))
                            tela.blit(texto_ajuda3, (20, 300))

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














