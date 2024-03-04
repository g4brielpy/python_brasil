'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''

vogais = ['a', 'e', 'i', 'o', 'u']
qtd_vogais = 0
qtd_espacos = 0

frase = input('Digite uma frase: ')

for letra in frase:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        qtd_vogais += 1
    elif letra == ' ':
        qtd_espacos += 1

print(f'\nQuantidade de vogais: {qtd_vogais}')
print(f'Quantidade de espaços: {qtd_espacos}')
