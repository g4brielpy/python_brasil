'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def somar(*valores):
    valores = list(valores)
    return sum(valores)

print(somar(1, 2, 3))