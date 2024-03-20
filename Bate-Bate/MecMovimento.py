import pygame
import random

class MovendoTexto:     # <- Criação de uma classe, obrigatoriamente precisa de __ dois underlines
    def __init__(self, texto, fonte_tamanho, largura, altura):          # def = Métodos
        self.fonte = pygame.font.SysFont(None, fonte_tamanho)   # Define o tipo da fonte, o tamanho e o estilo
        self.texto = texto         # Define o texto da Janela                         # Self = Atributos/Parâmetros
        self.largura = largura     # Define a largura da Janela     
        self.altura = altura       # Define a altura da Janela 
        # self.font.render(texto, True, (255,255,255)) atribuído a variável = self.text_surf
        self.texto_surf = self.fonte.render(texto, True, (255,255,255))     # Renderiza o texto na tela
        self.rect = self.texto_surf.get_rect(center=(largura/2, altura/2))  # Trás o retângulo envolta do texto centralizado 

        # Variáveis definidas com as velocidades iniciais aleatoriamente não nulas
        self.velocidade_x = self.gerar_numero_nao_zero()
        self.velocidade_y = self.gerar_numero_nao_zero()

    def gerar_numero_nao_zero(self):            # Criação do método (gerar_numero_nao_zero) número aleatório não nulo
        numero = 0          # Variável iniciliazada como zero
        while numero == 0:  # Enquanto o número o numero gerado for zero, continue gerando
            numero = random.randint(-1, 1)  # Roda um número aleatório entre -1 e 1
        return numero       # Retorna o número gerado

    def move(self):         # Definição de um método para mover o texto
        self.rect.x += self.velocidade_x    # Atualiza as coordenadas do retângulo do texto com base nas velocidades
        self.rect.y += self.velocidade_y

        # Verifica se o texto atingiu as bordas da tela e atualiza as velocidades e cores do texto, se necessário
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

        if self.rect.bottom >= self.altura:
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(-1, 0)
            self.change_color()

    def change_color(self):     # Definição de um método para mudar a cor do texto
        cor_texto = (           # Gera cor aleatória
        random.randint(0, 255), 
        random.randint(0, 255), 
        random.randint(0, 255),
    )
        self.texto_surf = self.fonte.render(self.texto, True, cor_texto)    # Renderiza nova cor no texto

    
