# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name


# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
	# Método Construtor
    def __init__(self, palavara):
        self.palavra = palavara 
        self.letras_erradas = []
        self.letras_escolhidas = []

	# Método para adivinhar a letra
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
            return True
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
            
        return False
        
	# Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) ==6)
	# Método para verificar se o jogador venceu
    def hangman_won(self):
        if "_" not in self.hide_palavra():
            return True
        return False
	# Método para não mostrar a letra no board
    def hide_palavra(self):
        rtn = ""
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn+='_'
            else:
                rtn+= letra
        return rtn
	# Método para checar o status do game e imprimir o board na tela
    def print_check(self):
        print(board[len(self.letras_erradas)])
        
        print(f'\nPalavra: {self.hide_palavra()}')

        print(f'Letras Erradas: ')
        
        for letra in self.letras_erradas:
            print(letra,)
        print()
        print("Letras Corretas: ")
        for letra in self.letras_escolhidas:
            print(letra,)
def limpa_tela():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')
def pergunta_letra():
    letra = str(input("Qual a letra? ")).lower()
    return letra
# Método para ler uma palavra aleatoria do banco de palavras
def carregar_palavra():
    palavras = []
    with open("Jogo da Forca/palavras.txt", "r", encoding="utf8") as arquivo:
        dados = arquivo.read()
        palavras = list(dados.split(',\n'))
    palavra_aleatoria = random.choice(palavras)
    return palavra_aleatoria

def main():
    limpa_tela()
    game = Hangman(carregar_palavra())
    while not game.hangman_over():
        game.print_check()
        letra = pergunta_letra()
        game.guess(letra)
    game.print_check()
    if game.hangman_won():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(game.palavra))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        
        
        
if(__name__ == '__main__'):
    main()