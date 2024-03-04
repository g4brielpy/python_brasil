'''
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
'''

from num2words import num2words

while True:
    try:
        numero: int = int(input('Digite um número até 99: '))
    except Exception as e:
        print(f'Erro: {e}\n')
    else:
        break

numero_extedo_ptbr: str = num2words(numero, lang='pt-br')

print(f'Número {numero} por extenso: {numero_extedo_ptbr}')
