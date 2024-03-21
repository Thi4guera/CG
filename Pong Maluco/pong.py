import pygame
import sys      # Inicializa os atributos do pygame

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
pc_y = altura // 2 - raquete_altura // 2   # Definição da posição da altura da raquete

# Posição da Raquete do player
player_1_x = largura - 20    # 800 - 5 = 795
player_1_y = altura // 2 - raquete_altura // 2

# Posição da bola
bola_x = largura // 2 - tamanho_bola // 2
bola_y = altura // 2 - tamanho_bola // 2

raquete_player_1_dy = 5
raquete_pc_dy = 5

clock = pygame.time.Clock()


# Loop infinito
rodando = True
while rodando:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:   # Verifica se o evento é clicado para fechar a janela
            rodando = False             # Variável rodando como False para sair do jogo

    screen.fill(PRETO)                  # Cor do fundo da tela

    pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raquete_largura, raquete_altura))
    pygame.draw.rect(screen, BRANCO, (player_1_x, player_1_y, raquete_largura, raquete_altura))
    pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, tamanho_bola, tamanho_bola))

    keys = pygame.key.get_pressed()      # Vai criar uma variável que vai pegar uma função método que vai ouvir o teclado

    if keys[pygame.K_UP] and player_1_y > 0:
        player_1_y -= raquete_player_1_dy
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:
        player_1_y += raquete_player_1_dy


    pygame.display.flip()

    clock.tick(120)

pygame.quit()
sys.exit()          # Para liberar memória




