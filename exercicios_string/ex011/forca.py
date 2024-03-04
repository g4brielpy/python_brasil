'''
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''

from random import choice
import os


def buscar_palavras() -> list:
    # Obtém o caminho absoluto do script
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    # Constrói o caminho completo para 'palavras.txt'
    caminho_arquivo = os.path.join(diretorio_atual, 'palavras.txt')

    palavras: str = ''

    with open(caminho_arquivo, 'r') as arquivo:
        palavras = '\n'.join(arquivo)

        lista_palavras = palavras.split('\n')
        lista_palavras = [palavra for palavra in lista_palavras if palavra]

    return lista_palavras


def escolher_palavra() -> str:
    palavras = buscar_palavras()
    return (choice(palavras))


def verificar_letra(letra: str) -> str:
    if letra:

        if letra not in letras_escolhidas:
            letras_escolhidas.append(letra)

            if letra in PALAVRA:
                for index in range(len(palavra_oculta)):
                    if letra == PALAVRA[index]:
                        palavra_oculta[index] = letra
                if PALAVRA == palavra_oculta:
                    return 'Ganhou'

                return 'Acertou'
            else:
                return 'Erro'
        else:
            return 'Letra repetida'

    else:
        raise Exception


PALAVRA: list = list(escolher_palavra())
palavra_oculta: list = ['_' for _ in PALAVRA]
letras_escolhidas: list = []

tentativas: int = 1
tentativas_disponiveis: int = 6

while tentativas_disponiveis != 0:
    print('\n----- JOGO DA FORCA -----')
    print(f'Tentativas disponíveis: {tentativas_disponiveis}')
    try:
        letra: str = input('Digite uma letra: ').lower().strip()
        resposta = verificar_letra(letra)
        os.system('cls')
    except Exception:
        print('Erro! Digite um valor válido!')
    else:
        match resposta:
            case 'Ganhou':
                print(f'Você ganhou! A palavra é:', ''.join(
                    letra for letra in palavra_oculta))
                tentativas_disponiveis = 0

            case 'Acertou':
                print('A palavra é:', ' '.join(
                    letra for letra in palavra_oculta))

            case 'Erro':
                tentativas_disponiveis -= 1
                print(f'Você errou pela {tentativas}ª vez. Tente de novo!' if tentativas_disponiveis != 0 else 'Você perdeu!')
                tentativas += 1

            case 'Letra repetida':
                print('Letra repetida!')
else:
    print('\nJOGO FINALIZADO')
