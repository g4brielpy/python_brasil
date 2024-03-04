'''
Faça um Programa para um caixa eletrônico
PASSOS:
    1. O programa deverá perguntar ao usuário a valor do saque
    2. Informar quantas notas de cada valor serão fornecidas. 

OBS:
    As notas disponíveis serão as de 2, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
'''

'''controle = True

while controle:
    valor = float(input("Digite um valor: "))

    if valor >= 10 and valor <= 600:
        notas_100 = valor // 100
        valor = valor % 100

        notas_50 = valor // 50
        valor = valor % 50

        notas_10 = valor // 10
        valor = valor % 10

        notas_5 = valor // 5
        valor = valor % 5

        notas_2 = valor // 2
        valor = valor % 2

        notas_1 = valor // 1
        print(
            f"""
        Total de Notas de R$ 100: {notas_100*100}
        Total de Notas de R$ 50: {notas_50*50}
        Total de Notas de R$ 10: {notas_10*10}
        Total de Notas de R$ 5: {notas_5*5}
        Total de Notas de R$ 2: {notas_2*2}
        Total de Notas de R$ 1: {notas_1*1}
        """
        )
    else:
        print("Valor inválido. Tente novamente!")'''
        

from os import system

controle = True
MENU = '''
CAIXA ELETRÔNICO - BANCO NACIONAL
[1] - Sacar
[2] - Sair
=> '''

while controle:
    opcao = input(MENU)

    match opcao:
        case '1':
            valor = float(input("Digite um valor: "))

            if valor >= 10 and valor <= 600:
                notas_100 = valor // 100
                valor = valor % 100

                notas_50 = valor // 50
                valor = valor % 50

                notas_10 = valor // 10
                valor = valor % 10

                notas_5 = valor // 5
                valor = valor % 5

                notas_2 = valor // 2
                valor = valor % 2

                notas_1 = valor // 1
                print(
                    f"""
                Total de Notas de R$ 100: {notas_100*100}
                Total de Notas de R$ 50: {notas_50*50}
                Total de Notas de R$ 10: {notas_10*10}
                Total de Notas de R$ 5: {notas_5*5}
                Total de Notas de R$ 2: {notas_2*2}
                Total de Notas de R$ 1: {notas_1*1}
                """
                )
            else:
                print("Valor inválido. Tente novamente!")
                
            input("Aperte ENTER para continuar...")
            system("cls")
        case '2':
            controle = False
        case _:
            print('Opção inválida!')
