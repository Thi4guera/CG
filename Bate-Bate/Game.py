import pygame                                   # Importando de novo, porque está fora da classe
import sys
from MecMovimento import MovendoTexto           # from = olha o arquivo e (importa a Classe)

class Game:
    def __init__(self):
        pygame.init()
        self.largura = 800
        self.altura = 600
        self.tela = pygame.display.set.mode((self.largura, self.altura))
        pygame.display.set_caption("Bate-Bate")
        self.clock = pygame.time.Clock()
        self.MovendoTexto = MovendoTexto("Thiaguera", 50, self.largura, self.altura) # Instanciando a classe, 
                                                                                     #chamando ela para o Game

    def run(self):
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                
                self.MovendoTexto.move()            # Roda a função move da classe MovendoTexto
                self.tela.fill((0, 0, 0))           # Tela Preta
                self.tela.blit(self.MovendoTexto.texto_surf,    #Vai mostrar em tela
                                self.MovendoTexto)
                pygame.display.flip()
                self.clock.tick(60)

        pygame.quit()
        sys.exit()