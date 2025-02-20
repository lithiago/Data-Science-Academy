import numpy as np
from os import system, name
from time import sleep
from random import randint
jogadores = {
    "jogador1": '',
    "jogador2": ''
}

def iniciar_tabuleiro():
    tab = np.full((3,3), '', dtype=object)
    return tab

def fim_de_jogo(tab):
    matrix = np.zeros((3,3))
    
    # Obtendo posições de X e O no tabuleiro
    linhas_X, cols_X = np.where(tab == 'X')  
    linhas_O, cols_O = np.where(tab == 'O')  

    # Preenchendo a matriz com 1 para 'X' e -1 para 'O'
    matrix[linhas_X, cols_X] = 1  
    matrix[linhas_O, cols_O] = -1  

    # Verifica vitória nas diagonais
    if np.fliplr(matrix).diagonal().sum() == -3 or np.diagonal(matrix).sum() == -3:
        return ("Jogador 1" if jogadores['jogador1'] == "O" else "Jogador 2"), True

    if np.fliplr(matrix).diagonal().sum() == 3 or np.diagonal(matrix).sum() == 3:
        return ("Jogador 1" if jogadores['jogador1'] == "X" else "Jogador 2"), True

    # Verifica vitória nas linhas e colunas
    if 3 in np.sum(matrix, axis=1) or 3 in np.sum(matrix, axis=0):
        return ("Jogador 1" if jogadores['jogador1'] == "X" else "Jogador 2"), True

    if -3 in np.sum(matrix, axis=1) or -3 in np.sum(matrix, axis=0):
        return ("Jogador 1" if jogadores['jogador1'] == "O" else "Jogador 2"), True

    # Se ninguém venceu, retorna sem vencedor
    return "", False
    
def colocar_no_tabuleiro(simbolo, tab):
    while True:
        try:
            linha = int(input("Seleciona uma linha: ")) - 1 
            coluna = int(input("Seleciona uma coluna: ")) - 1
            if(linha <= tab.shape[0] and coluna <= tab.shape[1]):
                if(tab[linha][coluna] == ''):
                    tab[linha][coluna] = simbolo
                    break
                print('Posição já ocupada!')
            else:
                print("Selecione uma posição dentro dos limites do tabuleiro")
        except:
            print("Selecione um valor númerico")
    print(tab)
    return tab

def imprime_mensagem():
    print("*********************************")
    print("***Bem vindo ao Jogo da Velha!***")
    print("*********************************")

def inica_jogo():
    print("O jogo está começando!")
    for i in range(3,0,-1): # De 3 a 1
        sleep(1)
        print(i)
def exibir_tabuleiro(tab):
    for i in range(3):
        linha_formatada = " | ".join(tab[i])  # Junta os elementos da linha com " | "
        print(f" {linha_formatada} ")  
        if i < 2:  # Adiciona a linha divisória apenas entre as linhas
            print("---+---+---")
def limpa_tela():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print(f"JOGADOR 1: {jogadores['jogador1']} \t JOGADOR 2: {jogadores['jogador2']} \n")
def jogar():
    imprime_mensagem()
    
    while True:
        try:
            jogadores["jogador1"] = str(input('Jogador 1 selecione entre [X|O]: ')).upper().strip()
            jogadores["jogador2"] = "X" if jogadores["jogador1"] == "O" else "O"
            selecionados = np.array(list(jogadores.values())) 
            if np.all(np.isin(["X", "O"], selecionados)):
                break
            print("Selecione uma opção válida")
        except:
            print("Opção Inválida!")
    terminou = False
    limpa_tela()
    inica_jogo()
    
    vez_do_jogador = randint(1,2)
    print(f"\n\nJogador {vez_do_jogador} começa!\n\n")
    tab = iniciar_tabuleiro()        
    while terminou == False:
        exibir_tabuleiro(tab)
        if vez_do_jogador == 1:
            colocar_no_tabuleiro(jogadores["jogador1"], tab)
            vez_do_jogador = 2
        elif vez_do_jogador == 2:
            colocar_no_tabuleiro(jogadores['jogador2'], tab)
            vez_do_jogador = 1
        vencedor, terminou = fim_de_jogo(tab)
        limpa_tela()
        print(f"Vez do Jogador{vez_do_jogador}\n\n")

    print(f"Parabéns {vencedor}, você ganhou!")
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


if(__name__ == '__main__'):
    jogar()



    