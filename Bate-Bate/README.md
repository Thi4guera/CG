Projeto Bate-Bate baseado no display do DVD movendo um texto de forma aleatória batendo sobre os cantos e trocando de dor aleatoriamente.

O Projeto foi divido em três etapas: Mecânica de Movimento, Main e Game. Cada parte possui seus respectivos "Atributos" e "Métodos".

========================================
<h1>Diagrama UML<h1>

<div align=center>

<img height="200em" src="./img/diagrama.png">

</div>
========================================

Primeira Etapa - Arquivo MecMovimento.py / Classe MovendoTexto

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

========================================

Segunda Etapa - Arquivo Game.py

Atributos:

self.largura: Define a largura da janela do jogo, definida com 800 pixels.

self.altura: Define a altura da janela do jogo, definida com 600 pixels.

self.tela: Define a criação da tela com a dimensões especificadas, com 600 de altura e 800 de largura.

self.clock: Define o objeto clock que controla a taxa de quadros do game

self.MovendoTexto: Cria um objeto da classe MovendoTexto e passa as características da classe para o objeto criado.

Métodos:

__init__: Construtor da classe Game, inicializa os atributos.

run: Este método executa o jogo, deixando em um loop, movendo o texto na tela, até que o usuário feche a janela.

========================================

Terceira Etapa - Arquivo Main.py

Cria uma instância da classe Game e chama o método run() para iniciar a execução do jogo.