import pygame                                   # Importando de novo, porque está fora da classe
import sys
from MecMovimento import MovendoTexto           # from = olha o arquivo MecMovimento e importa a Classe MovendoTexto

class Game:
    def __init__(self):             # Self signica que é dele mesmo
        pygame.init()
        self.largura = 800          # Define a largura da tela do game
        self.altura = 600           # Define a altura da tela do game
        self.tela = pygame.display.set_mode((self.largura, self.altura))   # Cria a tela do game com as dimensões definidas
        pygame.display.set_caption("Bate-Bate")     # Define o título do janela do game
        self.clock = pygame.time.Clock()            # Define o objeto clock que controla a taxa de quadros do game
        self.MovendoTexto = MovendoTexto("Thiaguera", 50, self.largura, self.altura) # Instanciando a classe, chamando ela para o Game
                                                                                    

    def run(self):      # Define o método run da classe
        rodando = True  # Variável rodando como True, mostrando que o game está em execução
        while rodando:  # Início do loop enquanto o game está em execução
            for evento in pygame.event.get():   
                if evento.type == pygame.QUIT:  # Verifica se o evento é de fechar a janela
                    rodando = False     # Variável rodando como False para sair do jogo
                
            self.MovendoTexto.move()    # Roda a função move da classe MovendoTexto
            self.tela.fill((0, 0, 0))   # Define as cores do fundo da tela como todo preto
            self.tela.blit(self.MovendoTexto.texto_surf, self.MovendoTexto.rect)    # Desenha o texto em tela
            pygame.display.flip()       # Exibe as mudanças na tela
            self.clock.tick(300)        # Define a taxa de quadros do game para 300 por segundos  

        pygame.quit()
        sys.exit()