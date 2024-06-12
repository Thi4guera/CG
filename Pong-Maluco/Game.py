import pygame
import sys
import random
from MecMovimento import Racket, Ball
from pygame import mixer

# Configurações de cores
BLACK = (0, 0, 0)   # Define a cor preta
WHITE = (255, 255, 255) # Define a branca

# Inicialização do Pygame e do módulo de fontes
pygame.init()
pygame.font.init()

# Configurações da tela
width = 800     # Define a largura
height = 600    # Define a altura
screen = pygame.display.set_mode((width, height))   # Cria a tela com as dimensões
pygame.display.set_caption("Pong")  # Define o título da janela

# Configuração da fonte
font_file = "Pong-Maluco/font/PressStart2P-Regular.ttf"     # Define o caminho do arquivo
font = pygame.font.Font(font_file, 24)      # Carrega a fonte com tamanho 24

# Configuração da música no Jogo
mixer.music.load("Pong-Maluco/audio/jailbreak.mp3")     # Carrega o diretório do arquivo da música  
mixer.music.play(-1)    # Toca a música em loop infito
mixer.music.set_volume(0.05)    # Define o volume da música para 0.05

sound = mixer.Sound("Pong-Maluco/audio/Sound_A.wav")

clock = pygame.time.Clock()     # Criação do objeto clock

running = False     # Indica se o jogo está em execução
score_player_1 = 0  # Variável para armazenar a pontuação do jogador
score_pc = 0        # Variável para armazenar a pontuação do pc

# Configurações das raquetes e bola
racket_width = 10   # Define a largura da raquete em 10
racket_height = 60  # Define a altura da raquete em 60
ball_size = 10      # Define o tamanho da bola em 10

# Instanciando objetos Racket e Ball
# Cria as raquetes do jogador e do computador e a bola, posicionando-os e configurando suas velocidades iniciais.
pc_racket = Racket(10, height // 2 - racket_height // 2, racket_width, racket_height, 5)
player_racket = Racket(width - 20, height // 2 - racket_height // 2, racket_width, racket_height, 5)
bola = Ball(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, 5, 2)
bolas = [bola]      # Armazena a bola em uma lista

def main_menu():    # Função para exibir o menu principal do jogo
    global running  # Variável global rodando
    while True:     # Loop que verifica quando fechar a janela ou pressionar a barra de espaço
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
                    return

        screen.fill(BLACK)  # Preenche a tela com a cor preta
        texto_menu = font.render("Pong", True, WHITE)   # Renderiza o texto no centro da tela
        text_menu_rect = texto_menu.get_rect(center=(width // 2, height // 2))
        screen.blit(texto_menu, text_menu_rect)

        # Alterna o texto "Pressione Espaço" a cada segundo para piscar
        tempo = pygame.time.get_ticks() 
        if tempo % 2000 < 1000:
            texto_iniciar = font.render("Pressione Espaço", True, WHITE)
            texto_iniciar_rect = texto_iniciar.get_rect(center=(width // 2, 450))
            screen.blit(texto_iniciar, texto_iniciar_rect)

        pygame.display.flip()

def create_new_ball():  # Função para criar uma nova bola no centro da tela com velocidade aleatória e adiciona a lista
    new_ball = Ball(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, random.choice([-5, 5]), random.choice([-5, 5]))
    new_ball.change_color()
    bolas.append(new_ball)

def game_loop():    # Loop do jogo
    global running, score_player_1, score_pc
    start_time = pygame.time.get_ticks()    # Obtem o tempo atual quando o pygame é iniciado e armazena a variável no start_time
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Verifica se algum evento do tipo do clique no botão fechar ocorreu.
                running = False

        screen.fill(BLACK)

        current_time = pygame.time.get_ticks()
        if current_time - start_time > 10000:  # Criar nova bola a cada 10 segundos
            create_new_ball()
            start_time = current_time

        for bola in bolas:
            bola.move() # Chama o método move do objeto bola, que atualiza a posição da bola com base na sua velocidade atual.

            # Colisão da bola com as raquetes
            if bola.rect.colliderect(pc_racket.rect) or bola.rect.colliderect(player_racket.rect):
                bola.bounce('x')
                bola.change_color()
                sound.play()

            # Colisão da bola com as bordas da tela
            if bola.rect.top <= 0 or bola.rect.bottom >= height:
                bola.bounce('y')
                bola.change_color()

            # Pontuação e reposição da bola
            if bola.rect.left <= 0: # Verifica se a bola colide com a borda esquerda da tela (indicando que o jogador marcou um ponto)
                bola.reset_position(width // 2 - ball_size // 2, height // 2 - ball_size // 2)
                score_player_1 += 1
                print(f"Score Player_1: {score_player_1}")

            if bola.rect.right >= width:  # Verifica se a bola colide com a borda direita da tela (indicando que o PC marcou um ponto).
                bola.reset_position(width // 2 - ball_size // 2, height // 2 - ball_size // 2)
                score_pc += 1
                print(f"Score PC: {score_pc}")

            bola.draw(screen)   # Desenha a bola na tela na sua posição inicial

        # Movendo a raquete do pc
        pc_racket.follow_ball(bolas[0].rect.centery)

        # Movendo a raquete do player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_racket.move_up()
        if keys[pygame.K_DOWN]:
            player_racket.move_down(height)

        # Desenhando os objetos na tela
        pc_racket.draw(screen, WHITE)
        player_racket.draw(screen, WHITE)

        # Desenhando a linha central e o placar
        pygame.draw.aaline(screen, WHITE, (width // 2, 0), (width // 2, height))
        font_score = pygame.font.Font(font_file, 12)
        score_texto = font_score.render(f"Score PC: {score_pc}  Score Player: {score_player_1}", True, WHITE)
        score_rect = score_texto.get_rect(center=(width // 2, 24))
        screen.blit(score_texto, score_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
