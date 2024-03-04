'''
JOGO DA PALAVRA EMBARALHADA. 
Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
O jogador terá seis tentativas para adivinhar a palavra. 
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
'''

from random import choice, shuffle
import os


def embaralhar_palavra(palavra: str) -> str:
    letras: list = [letra for letra in palavra]
    shuffle(letras)

    palavra_embaralhada: str = ''.join(letras)

    return palavra_embaralhada


def buscar_palavras() -> str:
    # Obtém o caminho absoluto do script
    diretorio_atual: str = os.path.dirname(os.path.abspath(__file__))
    caminho_palavras: str = os.path.join(diretorio_atual, 'palavras.txt')

    with open(caminho_palavras, 'r') as arquivo:
        palavras: str = '\n'.join(arquivo)
        lista_palavras: list = palavras.split()

    return choice(lista_palavras)


def menu(palavra: str, tentativas: int) -> None:
    print('\nJOGO DA PALAVRA EMBARALHADA')
    print(f'Palavra embaralhada: {palavra}')
    print(f'Tentativas restantes: {tentativas}\n')


PALAVRA: str = buscar_palavras()
palavra_embaralhada: str = embaralhar_palavra(PALAVRA)


tentativas_disponiveis: int = 6
while tentativas_disponiveis != 0:
    menu(palavra_embaralhada, tentativas_disponiveis)
    chute: str = input('Chute: ')

    if chute == PALAVRA:
        print('Parabéns, você ganhou!')
        break

    os.system('cls')
    tentativas_disponiveis -= 1

    if not tentativas_disponiveis == 0:
        print('Tente novamente, você errou!')

else:
    print(f'Você perdeu! A palavra é {PALAVRA}')
