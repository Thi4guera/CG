import sys
import pygame
import random   #Pegando um pacote

# Inicializa o Pygame
pygame.init()

#Configuração da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

# Define as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
#VERMELHO = (255, 0, 0)
#AZUL = (0, 0, 255)
#AMARELO = (255, 255, 0)
#VERDE = (0, 255, 0)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Thiago", True, BRANCO)
texto_rect = texto.get_rect(center=(largura/2, altura/2)) #Centro (Renderiza o ponto e o retângulo no centro)
clock = pygame.time.Clock()
#texto_rect = texto.get_rect(center=(largura/2, 25)) #Topo
#texto_rect = texto.get_rect(center=(65, 25)) #Canto Superior Esquerdo
#texto_rect = texto.get_rect(center=(735, 25)) #Canto Superior Direito
#texto_rect = texto.get_rect(center=(65, 575)) #Canto Inferior Esquerdo
#texto_rect = texto.get_rect(center=(largura/2, 575)) #Base
#texto_rect = texto.get_rect(center=(735, 575))

#velocidade_x = 1    #Variável
#velocidade_y = 1

v_x = 0
v_y = 0

velocidade_x = random.randint(-1, 1)  #Para o nome sair aleatoriamente - Entre 1, 0 e -1
velocidade_y = random.randint(-1, 1)  #Função (randint)

while velocidade_x == 0:        #Enquanto tiver rodando zero, vai rodar de novo
    velocidade_x = random.randint(-1, 1)
while velocidade_y == 0:        #Enquanto tiver rodando zero, vai rodar de novo
    velocidade_y = random.randint(-1, 1)
                                #Quando rodar e não sair zero, ele vai pro LOOP PRINCIPAL

#A renderização da tela começa do lado esquerdo para o direito
#Para posicionar o retângulo invísivel no ponto inicial do lado esquerdo, ao invés de posicionar o retângulo 
#invísivel no centro, sem ter que ficar modificando a cordenada (largura e altura), como nos comandos acima

#texto_rect = texto.get_rect()  #O get ele pega o referência, cria o objeto
#texto_rect.left = 0 #Canto superior esquerdo, posiciona o retângulo do lado esquerdo
#texto_rect.top = 0  #No topo

#texto_rect.left = 0 #Canto inferior esquerdo, posicionar o retângulo do lado esquerdo
#texto_rect.bottom = 600 #Parte debaixo

#texto_rect.right = 800 #Canto inferior direito, posicionar o retângulo do lado de baixo na direita
#texto_rect.bottom = 600 #Parte debaixo

#texto_rect.right = 800 #Canto superior direito
#texto_rect.top = 0

#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    texto_rect.x += velocidade_x   #Leva o texto para direita (+= incremento, a cada rodada soma 1)
    
    texto_rect.y += velocidade_y

    # Verifica se o texto atinge as bordas da tela
    #if texto_rect.right >= largura or texto_rect.left <= 0:
    if texto_rect.right >= largura:
       #velocidade_x = -velocidade_x
       velocidade_x = random.randint(-1, 0)
       velocidade_y = random.randint(-1, 1)
       cor_texto = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
       texto = fonte.render("Thiago", True, cor_texto)

    #if texto_rect.bottom >= altura or texto_rect.top <= 0:
    if texto_rect.bottom >= altura:
        #velocidade_y = -velocidade_y
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 0)
        cor_texto = (random.randint(0, 255),                # random.randint(0, 255     Sorteia as cores quando
                     random.randint(0, 255),                # random.randint(0, 255     bate nos cantos
                     random.randint(0, 255))                # random.randint(0, 255
        texto = fonte.render("Thiago", True, cor_texto)
    
    if texto_rect.top <= 0:
        #velocidade_y = -velocidade_y
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(0, 1)
        cor_texto = (random.randint(0, 255), 
                     random.randint(0, 255), 
                     random.randint(0, 255))
        texto = fonte.render("Thiago", True, cor_texto)

    if texto_rect.left <= 0:
        #velocidade_x = -velocidade_x
        velocidade_x = random.randint(0, 1)
        velocidade_y = random.randint(-1, 1)
        cor_texto = (random.randint(0, 255), 
                     random.randint(0, 255), 
                     random.randint(0, 255))
        texto = fonte.render("Thiago", True, cor_texto)

    clock.tick(700) #Definindo FPS
    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()

