Projeto Bate-Bate baseado no display do DVD

Projeto foi divido em três etapas: Mecânica de Movimento, Main e Game. Cada parte possui seus respectivos "Atributos" e "Métodos"

========================================
<h1>Diagrama UML<h1>

<div align=center>

<img height="200em" src="./img/diagrama.jpg">

</div>
========================================

Arquivo MecMovimento.py

Atributos:

self.fonte: Define a fonte do texto, o tipo, tamanho e estilo que vai aparecer para o usuário

self.texto: Define o texto que será exibido na tela

self.largura: Define a largura da janela 

self.altura: Define a altura da janela

self.texto_surf: Define a superfície e renderiza o texto na tela

self.rect: Define a área em que o texto aparecerá em forma de retângulo usando como base a largura e altura, trazendo centralizado

self.velocidade_x: Define uma variável com a velocidade inicial aleatoriamente não nula na horizontal do jogo

self.velocidade_y: Define uma variável com a velocidade inicial aleatoriamente não nula na vertifcal do jogo

Métodos:

__init__: Método de criação da classe, inicializa todos os atributos

def gerar_numero_nao_zero: Gera um número aleatório não nulo

def move: Move o texto na tela e atualiza as coordenadas do retângulo do texto com base nas velocidades

def change_color: Gera uma cor aleatória e atribuí ela no texto
