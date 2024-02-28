import sys
import pygame

pygame.init()

#Configuração da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Thiago", True, BRANCO)
#texto_rect = texto.get_rect(center=(largura/2, altura/2)) #Centro
#texto_rect = texto.get_rect(center=(largura/2, 25)) #Topo
#texto_rect = texto.get_rect(center=(65, 25)) #Canto Superior Esquerdo
#texto_rect = texto.get_rect(center=(735, 25)) #Canto Superior Direito
#texto_rect = texto.get_rect(center=(65, 575)) #Canto Inferior Esquerdo
#texto_rect = texto.get_rect(center=(largura/2, 575)) #Base
texto_rect = texto.get_rect(center=(735, 575))

#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()
