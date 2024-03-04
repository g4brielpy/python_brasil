'''
VERIFICAÇÃO DE CPF. 
Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e 
indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
'''


def validar_formato(cpf: str):
    if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
        if cpf[:3].isdigit() and cpf[4:7].isdigit() and cpf[8:11].isdigit() and cpf[12:].isdigit():
            return True

    return False


cpf: str = input('Digite seu CPF no formato "xxx.xxx.xxx-xx": ')
print('CPF váldio' if validar_formato(cpf) else 'CPF inválido')
