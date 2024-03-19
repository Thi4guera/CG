from Game import Game         # from Game (importa do arquivo - Game) / importa Game (importa a classe Game)

if __name__ == "__main__":    # Verifica se este módulo está sendo executado como o programa principal  
    Game = Game()             # Instanciando do objeto, pega os métodos todos da classe
    Game.run()                # Chama o método run da instância game para executar o início do jogo