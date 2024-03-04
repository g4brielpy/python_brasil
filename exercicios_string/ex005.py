'''
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
'''

nome = input('Digite seu nome: ')

index = len(nome)
for i in range(len(nome)+1):
    print(nome[:index])
    index -= 1
