import pygame
import random

class Racket:   # Define a classe da Raquete
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)    # Criação de um retângulo com as posições x e y e largura e altura da raquete
        self.speed = speed  # Define a velocidade da raquete

    def move_up(self):  # Função para mover a raquete para cima
        if self.rect.top > 0:   # Verifica se a raquete chega até o topo (limite da tela)
            self.rect.y -= self.speed   # Move a raquete para cima diminuindo y pelo valor da velocidade

    def move_down(self, boundary_height):   # Função para mover a raquete para baixo
        if self.rect.bottom < boundary_height:  # Verifica se a raquete  chega até em baixo (limite da tela)
            self.rect.y += self.speed   # Move a raquete para baixo aumentando y pelo valor da velocidade

    def follow_ball(self, ball_y):  # Raquete siga a posição da bola
        if self.rect.centery < ball_y:  # Se o centro da raquete está acima da posição y da bola
            self.rect.y += self.speed   # move a raquete para baixo
        elif self.rect.centery > ball_y:    # Se estiver abaixo da posição y da bola
            self.rect.y -= self.speed       # move a raquete para cima

    def draw(self, screen, color):  # Desenha a raquete na tela
        pygame.draw.rect(screen, color, self.rect)  # Desenha um retângulo na tela e a cor

class Ball: # Criação da classe Bola
    def __init__(self, x, y, size, speed_x, speed_y):   # __init__ construtor da classe
        self.rect = pygame.Rect(x, y, size, size)   # Cria um retângulo com as posições x e y, e o tamanho da bola
        self.speed_x = speed_x  # Define velocidade x da bola
        self.speed_y = speed_y  # Define velocidade y da bola
        self.color = (255, 255, 255)    # Define a bola com a cor branca

    def move(self): # Função de mover a bola
        self.rect.x += self.speed_x # Move a bola na direção x
        self.rect.y += self.speed_y # Move a bola na direção y

    def bounce(self, axis): # Faz a inversão da bola quando colide com a raquete ou os cantos da tela
        if axis == 'x': # Se bater no eixo x, inverte a velocidade x
            self.speed_x = -self.speed_x
        elif axis == 'y':   # Se bater no eixo y, inverte a velocidade y
            self.speed_y = -self.speed_y

    def reset_position(self, x, y): # Função para resetar a posição da bola e inverter a direção
        self.rect.x = x # Define a nova posição x da bola
        self.rect.y = y # Define a nova posição y da bola
        self.bounce('x')    # Inverte a direção x   

    def change_color(self): # Mudar a cor da bola aleatoriamente
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 

    def draw(self, screen): # Desenha a bola na tela com uma cor
        pygame.draw.ellipse(screen, self.color, self.rect)
