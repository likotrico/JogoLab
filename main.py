from random import randint
from pygame.locals import *
from sys import exit
from funcoesJogo import *
from Menu_Principal import *
from sprites import *

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

#Formando a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Campo Minado') # Nome da Janela do jogo

rodarAnimacaoInicial(tela) #Rodar a animação

menu = -1 #Variável que ficará responsável pelo loop do menu

while menu != 0:
    menu = rodarMenu(tela)  # Mostrar o display do Menu
    dimensoes = menu #Escolher as dimensões de acordo com a dificiltado escolhida.
                     #Obs: a função rodarMenu retorna o valor das dimensões ou 0 para não entrar nos loops do jogo
    if dimensoes != 0:
        gameloop = True #Variável para saber se vai voltar a jogar ou não quando a partida termina
        jogando = True #Variável para estar jogando
        decisao = True
    else:
        gameloop = False
        jogando = False
        decisao = False
    while gameloop:
        # Dimensão que pode ser alterada
        if dimensoes == 8:
            qtd_bombas = dimensoes + 1
            bandeiras = qtd_bombas
        elif dimensoes == 16:
            qtd_bombas = 25
            bandeiras = qtd_bombas
        bombas_restante = qtd_bombas

        # Organizando fonte
        tamanho_fonte = 0
        if dimensoes == 8:
            tamanho_fonte = 40
        else:
            tamanho_fonte = 20

        fonte = pygame.font.SysFont('arial', tamanho_fonte, False, False)
        fonte2 = pygame.font.SysFont('arial', 40, True, True)
        fonte3 = pygame.font.SysFont('arial', 50, False, False)

        newLarg = int((largura) / dimensoes)  # Largura das Células
        newAlt = int((altura - 100) / dimensoes)  # Altura das Células
        matriz = gerarMatriz(dimensoes)  # Matriz que vai armadezar todas as informações de uma dada célula
        gerarTabuleiro(matriz, largura, altura, dimensoes)  # Alterar a matriz com todas as informações necessárias

        objetos = []  # Lista dos objetos que serão utilizados para colisões

        # For que gera os objetos para colisão e os coloca na lista de objetos
        for i in matriz:
            for j in i:
                xy = j.rect
                obj_aux = pygame.draw.rect(tela, (0, 0, 0), (xy[0], xy[1], newLarg, newAlt))
                objetos.append(obj_aux)
            obj_aux = []

        qtd_reveladas = 0
        vitoria = -1
        um_valorai = []
        first_play = True

        relogio = iniciarContagem()

        while jogando:
            # Informações da localização do mouse
            tela.fill(preto)
            coordrato = pygame.mouse.get_pos()
            rato = pygame.draw.rect(tela, (0, 0, 0), (coordrato[0], coordrato[1], 1, 1))

            printMatriz(matriz, tela, largura, altura, dimensoes)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #REVELAR A CÉLULA
                    if pygame.mouse.get_pressed() == (1,0,0):
                        print(coordrato)
                        for i in objetos:
                            if i.colliderect(rato):
                                for linha in matriz:
                                    for elemento in linha:
                                        vetor = [i[0], i[1]]
                                        if vetor == elemento.rect:
                                            if elemento.cond == 0:
                                                elemento.cond = 1
                                                um_valorai = elemento.rect
                                                if qtd_reveladas >= 1 and elemento.bomb == 0:
                                                    revelarAdjacentes(um_valorai, matriz)
                    #MARCAR A CÉLULA COM A BANDEIRA
                    if pygame.mouse.get_pressed() == (0,0,1):
                        print(coordrato)
                        for i in objetos:
                            if i.colliderect(rato):
                                for linha in matriz:
                                    for elemento in linha:
                                        vetor = [i[0], i[1]]
                                        if vetor == elemento.rect:
                                            if elemento.cond == 0 and bandeiras > 0:
                                                elemento.cond = 2
                                                bandeiras -= 1
                                            elif elemento.cond == 2:
                                                elemento.cond = 0
                                                bandeiras += 1

            # Informações bandeiras
            msg_bandeiras = f'Bandeiras: {bandeiras}'
            texto_bandeiras = fonte3.render(msg_bandeiras, True, verde)
            tela.blit(texto_bandeiras, (10, 15))

            # Informações relogio
            msg_relogio = f'Tempo: %.f'%(atualizarContagem(relogio))
            texto_relogio = fonte3.render(msg_relogio, True, verde)
            tela.blit(texto_relogio, (380, 15))

            # Condição para que a primeira casa revelada não contenha bomba
            if first_play == True and qtd_reveladas == 1:
                print('first play')
                # Preenchendo a matriz com as bombas
                while qtd_bombas != 0:
                    x_random = randint(0, dimensoes - 1)
                    y_random = randint(0, dimensoes - 1)
                    if matriz[x_random][y_random].bomb == 0 and matriz[x_random][y_random].cond != 1:
                        matriz[x_random][y_random].bomb = 1
                        qtd_bombas = qtd_bombas - 1
                rastreamento(matriz)
                revelarAdjacentes(um_valorai, matriz)
                print('passou essa linha')
                first_play = False

            #IMPRIMIR AS MINAS DETECTADAS NAS CÉLULAS REVELADAS
            contador = 0 #Variável para ajudar na condição de vitória
            for linha in matriz:
                for elemento in linha:
                    informação_mina_detectada = f'{elemento.rast}'
                    texto_mina_detectada = fonte.render(informação_mina_detectada, True, azul)
                    informação_bomba = f'{elemento.bomb}'
                    texto_bomba = fonte.render(informação_bomba, True, verde)
                    if elemento.bomb == 1 and elemento.cond == 1: #Verificando se Perdeu
                        vitoria = 0
                        printarNumero(matriz, tela, newLarg, newAlt, texto_bomba, elemento.rect, dimensoes)
                        jogando = False
                    elif elemento.cond == 1:
                        if elemento.rast != 0:
                            printarNumero(matriz, tela, newLarg, newAlt, texto_mina_detectada, elemento.rect, dimensoes)
                    if elemento.cond == 1: #Contando as células reveladas
                        contador += 1

            qtd_reveladas = contador #Adquirindo o valor das células reveladas
            if qtd_reveladas + bombas_restante == dimensoes * dimensoes: #Verificando se ganhou
                vitoria = 1
                jogando = False

            pygame.display.update()

        decisao = True
        while decisao:
            printMatriz(matriz, tela, largura, altura, dimensoes)

            if vitoria == 1:
            #Revelando a última célula revelada (Evitar Bug visual)
                for linha in matriz:
                    for elemento in linha:
                        informação_mina_detectada = f'{elemento.rast}'
                        texto_mina_detectada = fonte.render(informação_mina_detectada, True, azul)
                        if elemento.cond == 1:
                            if elemento.rast != 0:
                                printarNumero(matriz, tela, newLarg, newAlt, texto_mina_detectada, elemento.rect, dimensoes)
                #Texto de vitória
                msg_vitoria = 'Parabéns, você ganhou!'
                texto_vitoria = fonte2.render(msg_vitoria, True, branco)
                #Desenhando os retângulos de arte
                pygame.draw.rect(tela, branco, (125, 225, 390, 60))
                pygame.draw.rect(tela, preto, (130, 230, 380, 50))
                #Imprimindo na tela o texto pós-game
                tela.blit(texto_vitoria, (130, 230))

            elif vitoria == 0:
                #Mostrando onde estavam as outras bombas para o jogador
                for linha in matriz:
                    for elemento in linha:
                        informação_mina_detectada = f'{elemento.rast}'
                        texto_mina_detectada = fonte.render(informação_mina_detectada, True, azul)
                        informação_bomba = f'{elemento.bomb}'
                        texto_bomba = fonte.render(informação_bomba, True, verde)
                        if elemento.bomb == 1:
                            printarNumero(matriz, tela, newLarg, newAlt, texto_bomba, elemento.rect, dimensoes)
                        elif elemento.bomb == 0 and elemento.cond == 1 and elemento.rast != 0:
                            printarNumero(matriz, tela, newLarg, newAlt, texto_mina_detectada, elemento.rect, dimensoes)

                #Texto de derrota
                msg_derrota = 'Você perdeu!'
                texto_derrota = fonte2.render(msg_derrota, True, branco)
                #Retângulos para arte
                pygame.draw.rect(tela, branco, (125, 225, 390, 60))
                pygame.draw.rect(tela, preto, (130, 230, 380, 50))
                #Imprimindo na tela o texto pós-game
                tela.blit(texto_derrota, (215, 230))

            #Textos continuar e sair
            msg_continuar = 'Jogar novamente'
            msg_sair = 'Sair'
            texto_continuar = fonte2.render(msg_continuar, True, branco)
            texto_sair = fonte2.render(msg_sair, True, branco)

            #Retângulos para colisão continuar e sair
            rect_cont = pygame.draw.rect(tela, branco, (180, 295, 280, 60))
            pygame.draw.rect(tela, preto, (185, 300, 270, 50))

            rect_sair = pygame.draw.rect(tela, branco, (180, 365, 280, 60))
            pygame.draw.rect(tela, preto, (185, 370, 270, 50))

            tela.blit(texto_continuar, (185, 300))
            tela.blit(texto_sair, (280, 370))

            #Evento para continuar jogando ou sair
            coordrato = pygame.mouse.get_pos()
            rato = pygame.draw.rect(tela, (0, 0, 0), (coordrato[0], coordrato[1], 1, 1))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if rato.colliderect(rect_cont):
                    texto_continuar = fonte2.render(msg_continuar, True, verde)
                    tela.blit(texto_continuar, (185, 300))
                else:
                    texto_continuar = fonte2.render(msg_continuar, True, branco)
                    tela.blit(texto_continuar, (185, 300))
                if rato.colliderect(rect_sair):
                    texto_sair = fonte2.render(msg_sair, True, verde)
                    tela.blit(texto_sair, (280, 370))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        if rect_cont.colliderect(rato):
                            jogando = True
                            decisao = False
                        elif rect_sair.colliderect(rato):
                            gameloop = False
                            decisao = False

                pygame.display.update()

        matriz.clear()
        objetos.clear()

    #pygame.quit()
    #exit()