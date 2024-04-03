import pygame
import sys      # Inicializa os atributos do pygame
import random

pygame.init()

PRETO = (0,0,0)
BRANCO = (255,255,255)

largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura))     # (()) = Tupla # Criação da tela (display)
pygame.display.set_caption("Pong")      # Nome da tela

# Definição da Raquete
raquete_largura = 10       # Definição da largura da raquete
raquete_altura = 60        # Definição da altura da raquete 
tamanho_bola = 10          # Definição do tamanho da bola

# Posição da Raquete do pc
pc_x = 10                   # Definição da posição da raquete do lado esquerdo, considerando 10 pixels de distância da borda 
pc_y = altura // 2 - raquete_altura // 2   # Definição da posição da altura da raquete / - é por causa da referência da raquete

# Posição da Raquete do player
player_1_x = largura - 20    # 800 - 5 = 795 / -20 porque a renderização é da esquerda pra direita, ou seja, conta os 10 da largura da raquete e mais os 10 da distância da parede
player_1_y = altura // 2 - raquete_altura // 2

# Posição da bola
bola_x = largura // 2 - tamanho_bola // 2
bola_y = altura // 2 - tamanho_bola // 2

# Velocidade da raquete
raquete_player_1_dy = 5
raquete_pc_dy = 5

# Velocidade da bola
velocidade_bola_x = 5
velocidade_bola_y = 2


# Define o Score
score_player_1 = 0
score_pc = 0

clock = pygame.time.Clock()

# Loop infinito
rodando = True
while rodando:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:   # Verifica se o evento é clicado para fechar a janela
            rodando = False             # Variável rodando como False para sair do jogo

    screen.fill(PRETO)                  # Cor do fundo da tela

    # Movendo a bola
    bola_x += velocidade_bola_x     # += significa incremento + 1
    bola_y += velocidade_bola_y

    # Retângulos de colisão
    bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola)
    raquete_pc_rect = pygame.Rect(pc_x, pc_y, raquete_largura, raquete_altura)
    raquete_player_1_rect = pygame.Rect(
        player_1_x, player_1_y, raquete_largura, raquete_altura
    )

    # Colisão da bola com a raquete do pc e a raquete do player
    if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(
        raquete_player_1_rect
     ):
        velocidade_bola_x = -velocidade_bola_x

    # Colisão da bola com as bordas da tela
    if bola_y <= 0 or bola_y >= altura - tamanho_bola: # Valida se a bola bate em cima ou embaixo e retorna para direção contrária
        velocidade_bola_y = -velocidade_bola_y
    
    # Posicionar a bola no início do jogo
    if bola_x <= 0:
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola // 2
        velocidade_bola_x = -velocidade_bola_x
        score_player_1 += 1
        print(f"Score Player_1: {score_player_1}")

    if bola_x >= largura - tamanho_bola // 2:
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola // 2
        velocidade_bola_x = -velocidade_bola_x
        score_pc += 1
        print(f"Score PC: {score_pc}")

    # Movendo a raquete do pc pra seguir a bola
    #if pc_y < bola_y:                           # Se o centro da raquete abaixo do centro da bola
    #    pc_y += raquete_pc_dy                   # Movimenta a raquete pra baixo
    #elif pc_y + raquete_altura // parte_raquete_x  > bola_y:  
    #    pc_y -= raquete_pc_dy                   # Movimenta a raqueta para cima

    # Deixando o player 1 jogando de forma automática
    #if player_1_y + raquete_altura // parte_raquete_y  < bola_y:
    #    player_1_y += raquete_player_1_dy             
    #elif player_1_y > bola_y:  
    #    player_1_y -= raquete_player_1_dy    

    #if player_1_y + raquete_altura // 2  < bola_y:
    #    player_1_y += raquete_player_1_dy             
    #elif player_1_y + raquete_altura // 2  > bola_y:  
    #    player_1_y -= raquete_player_1_dy                  

    # Evitar que a raquete do pc sair da área
    if pc_y < 0:
        pc_y = 0
    elif pc_y > altura - raquete_altura:
        pc_y = altura - raquete_altura

    # Evitar que a raquete do player sair da área
    if player_1_y < 0:
        player_1_y = 0
    elif player_1_y > altura - raquete_altura:
        player_1_y = altura - raquete_altura

    # Assets (objetos)
    pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raquete_largura, raquete_altura))
    pygame.draw.rect(screen, BRANCO, (player_1_x, player_1_y, raquete_largura, raquete_altura))
    pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, tamanho_bola, tamanho_bola))
    pygame.draw.aaline(screen, BRANCO, (largura // 2, 0), (largura // 2, altura)) # Desenha a linha na tela com a cor branca

    keys = pygame.key.get_pressed()      # Vai criar uma variável que vai pegar uma função método que vai ouvir o teclado

    if keys[pygame.K_UP] and player_1_y > 0:
        player_1_y -= raquete_player_1_dy
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:
        player_1_y += raquete_player_1_dy


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()          # Para liberar memória




