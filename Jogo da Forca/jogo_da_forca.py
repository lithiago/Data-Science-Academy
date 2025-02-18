# Definir a lista de palavras possíveis

# Escolher uma palavra aleatória da lista

# Criar uma lista vazia para armazenar as letras advinhadas

# Definir o número máximo de tentativaz permitidas

# Enquanto o número de tentativas não atingir o limite máximo:

    # Mostrar a palavra com uma série underscores, com as letras adivinhadas preenchidas nos espaços corretos
    # Pedir ao jogador que adivinhe uma letra
    # Verificar se a letra adivinhada está na palavra
    # Se a letra adivinhada está na palavra, adicionar a letra à lista de letras adivinhadas e atualizar a exibição da palavra
    # Se a letra adivinhada não está na palavra, reduzir o número de tentativas restantes e exibir mensagem de erro
    # Verificar se todas as letras da palavra foram adivinhadas
    # Se todas as letras adivinhdas, exibir a mensagem de vitória
    # Se o número de tentativas chegar a zero, exibir a mensagem "Você perdeu. A palavra era [palavra escolhida]" e encerrar o jogo.


import random
from os import system, name



def limpa_tela():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def carregar_palavra():
    palavras = []
    with open("Jogo da Forca/palavras.txt", "r", encoding="utf8") as arquivo:
        dados = arquivo.read()
        palavras = list(dados.split(',\n'))
    palavra_aleatoria = random.choice(palavras)
    return palavra_aleatoria
def pergunta_letra():
    letra = str(input("Qual a letra? ")).lower()
    return letra

def marca_acerto(letra, letras_descobertas, palavra):
    index = 0
    for caractere in palavra:
        if caractere == letra:
            print(f"{palavra}")
            letras_descobertas[index] = letra
        index +=1
    return letras_descobertas
def jogar():
    limpa_tela()
    imprime_mensagem()
    print("Advinhe a palavra abaixo:\n")
    palavra = carregar_palavra()
    letras_descobertas = ['_' for letra in palavra]
    erros = 0
    acertos = 0
    letras_erradas = []
    print(letras_descobertas)
    while(erros <=7 and letras_descobertas.count('_') > 0):
        desenha_forca(erros)
        letra = pergunta_letra()
        if (letra in palavra):
            letras_descobertas = marca_acerto(letra, letras_descobertas, palavra)
        else:
            erros +=1
            desenha_forca(erros)
            letras_erradas.append(letra)
            print(f"Chances Restantes:{7 - erros}\n")
        print(letras_descobertas)
        print("Letras erradas:", "".join(letras_erradas))
    if erros < 7:
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
        print("A palavra era {}".format(palavra))
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

def imprime_mensagem():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
 
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

    
if(__name__ == '__main__'):
    jogar()