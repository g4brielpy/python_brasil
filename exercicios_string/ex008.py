'''
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice-versa. 
Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. 
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
Faça um programa que leia uma seqüência de caracteres, mostre-a e diga se é um palíndromo ou não.
'''

def polindromo(palavra: str) -> str:
    palavra = palavra.replace(' ', '').strip()
    palavra_vice: str = palavra[::-1]
    
    if palavra.lower() == palavra_vice.lower():
        return f'A sequencia {palavra} é um Políndromo'
    return f'A sequencia {palavra} não é um Políndromo'


sequencia: str = input('Digite uma palavra para verificar se é um Políndromo: ')

print(polindromo(sequencia))

