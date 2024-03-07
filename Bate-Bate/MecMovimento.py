import pygame
import random

class MovendoTexto:     # <- Criação de uma classe, obrigatoriamente precisa de __ dois underlines
    def __init__(self, texto, fonte_tamanho, largura, altura):          # def = Métodos
        self.font = pygame.font.SysFont(None, fonte_tamanho)
        self.text = texto                                  # Self = Atributos/Parâmetros
        self.largura = largura          
        self.altura= altura
        # self.font.render(texto, True, (255,255,255)) atribuído a variável = self.text_surf
        self.text_surf = self.font.render(texto, True, (255,255,255))  
        self.rect = self.texto.surf.get_rect(center=(largura/2, altura/2))


        self.velocidade_x = self.gerar_numero_nao_zero()
        self.velocidade_y = self.gerar_numero_nao_zero()

    def gerar_numero_nao_zero(self):            # Criação da função (gerar_numero_nao_zero)
        numero = 0
        while numero == 0:
            numero = random.randint(-1, 1)
        return numero

    def move(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        if self.rect.left <= 0:
            self.velocidade_x = random.randint(0, 1)
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()
        
        if self.rect.right >= self.largura:
            self.velocidade_x = random.randint(-1, 0)
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()

        if self.rect.top <= 0:
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(0, 1)
            self.change_color()

        if self.rect.bottom <= self.altura:
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(-1, 0)
            self.change_color()

    def change_color(self):
        cor_texto = (
        random.randint(0, 255), 
        random.randint(0, 255), 
        random.randint(0, 255),
    )
        self.text_surf = self.font.render(self.texto, True, cor_texto)

    