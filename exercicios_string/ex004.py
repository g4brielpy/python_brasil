'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
    F
    FU
    FUL
    FULA
    FULAN
    FULANO
'''

nome = input('Digite seu nome: ')

index = 0
for i in range(len(nome)+1):
    print(nome[:index])
    index += 1
