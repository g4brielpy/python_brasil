'''
Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
'''

while True:
    try:
        numero: int = int(input('\nDigite um número: '))
    except ValueError:
        print('Valor inválido! Digite novamente.')
    except Exception:
        print(f'Erro! Digite novamente.')
    else:
        print(f'O número informado é: {numero}')
        break
