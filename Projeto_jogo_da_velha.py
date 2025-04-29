import random
from random import randint

espacos = [['', '', ''], ['', '', ''], ['', '', '']]

def linha(txt):
    largura = 60
    print('-='*30)
    print(f'\033[36m{txt.center(largura)}\033[m')
    print('-=' * 30)

def mostrar_tabuleiro():
    for linha in espacos:
        print('\033[34m |  \033[m'.join(linha))
    print()

def jogada_computador(simbolo_oposto):
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if espacos[linha][coluna] == '':
            espacos[linha][coluna] = simbolo_oposto
            break

def jogada_jogador(opção, simbolo):
    if 1 <= opção <= 9:
        linha = (opção - 1) // 3
        coluna = (opção - 1) % 3
        if espacos[linha][coluna] == '':
            espacos[linha][coluna] = simbolo
        else:
            print('Esta posição já está ocupada, tente novamente!')
            return False  # Retorna False se a jogada for inválida
    else:
        print('Opção inválida!')
        return False  # Retorna False se a jogada for inválida
    return True  # Retorna True se a jogada for válida

def verificar_vitoria(s):
    for linha in espacos:
        if all(celula == s for celula in linha):
            return True
    for coluna in range(3):
        if all(espacos[linha][coluna] == s for linha in range(3)):
            return True
    if all(espacos[i][i] == s for i in range(3)) or all(espacos[i][2-i] == s for i in range(3)):
        return True
    return False

def par_impar():
    while True:
        escolha = input('Escolha Par ou Ímpar [P/I]: ').strip().upper()
        if escolha in ['P', 'I']:
            break
        else:
            print('Opção inválida!')
    while True:
        valor = int(input('Escolha um valor entre 0 e 10: '))
        if 0 <= valor <= 10:
            break
        else:
            print('Valor fora do intervalo! Tente novamente!')

    computador = randint(1, 10)
    print(f'Computador mostrou o valor: {computador}')
    print()
    total = computador + valor
    print(f'A soma dos números escolhidos foi {total}!')

    resultado = 'Par' if total % 2 == 0 else 'Ímpar'

    if (resultado == 'Par' and escolha == 'P') or (resultado == 'Ímpar' and escolha == 'I'):
        print('Parabéns você ganhou! Você começa!')
        return False  # Retorna False para indicar que o jogador começa
    else:
        print('Computador ganhou! O computador começa!')
        return True  # Retorna True para indicar que o computador começa

# PROGRAMA PRINCIPAL
linha('JOGO DA VELHA')
print()
linha('Vamos jogar par ou ímpar para ver quem começa!')

computador_ganhou = par_impar()

simbolo = ' '
while simbolo not in 'XxOo':
    simbolo = input('\033[1mVocê quer Xis ou Bola [x/o]? \033[m').strip().upper()[0]
simbolo_computador = 'O' if simbolo == 'X' else 'X'  # Define o símbolo do computador
print()
print('''\033[1mEscolha a opção:\033[m 
    \033[34m[1] [2] [3]
    [4] [5] [6] 
    [7] [8] [9]\033[m''')
print()

while True:
    if not computador_ganhou:  # Jogador joga primeiro
        mostrar_tabuleiro()
        opção = int(input('Qual a posição você deseja jogar? '))
        if not jogada_jogador(opção, simbolo):  # Se a jogada for inválida, continua o loop
            continue

        if verificar_vitoria(simbolo):
            mostrar_tabuleiro()
            print('Você venceu!')
            break

        computador_ganhou = True  # Alterna para o computador jogar
    else:  # Computador joga primeiro
        jogada_computador(simbolo_computador)
        if verificar_vitoria(simbolo_computador):
            mostrar_tabuleiro()
            print('Computador venceu!')
            break

        computador_ganhou = False  # Alterna para o jogador jogar

    if all(celula != '' for linha in espacos for celula in linha):
        mostrar_tabuleiro()
        print('Empate!')
        break





