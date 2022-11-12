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
        if len(verificacoes) > 0:
            verificados.append([x_coord, y_coord])
            verificacoes.remove([x_coord,y_coord])

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

gameloop = True #Variável para saber se vai voltar a jogar ou não quando a partida termina
jogando = True #Variável para estar jogando

while gameloop:
    dimensoes = 16  # Dimensão que pode ser alterada
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

    while jogando:
        # Informações da localização do mouse
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
                                        if elemento.cond == 0:
                                            elemento.cond = 2
                                            bandeiras -= 1
                                        elif elemento.cond == 2:
                                            elemento.cond = 0
                                            bandeiras += 1

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

pygame.quit()
exit()