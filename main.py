from jogar import *

pygame.init()

largura = 640 # Largura da Tela
altura = 580 # Altura da Tela

#Formando a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Campo Minado') # Nome da Janela do jogo

rodarAnimacaoInicial(tela) #Rodar a animação
jogar(tela, largura, altura)

pygame.quit()
exit()