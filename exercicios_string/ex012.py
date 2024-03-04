'''
Valida e corrige número de telefone. 
Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. NÃO É PADRÃO
O usuário pode informar o número com ou sem o traço separador.

    Valida e corrige número de telefone
    Telefone: 3 461-0133
    Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
    Telefone corrigido sem formatação: 34610133
    Telefone corrigido com formatação: 3461-0133
'''


def formatar_numero(telefone: str) -> str:
    numero_sem_formatar: list = list(telefone)
    numero_formatado: list = list(telefone)
    mensagem: str = ''

    if len(numero_sem_formatar) == 8 and '-' in numero_sem_formatar:
        # adicionar o 3 na frente
        numero_formatado.insert(0, '3')
        mensagem = 'Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.\n'

    elif len(numero_sem_formatar) == 8 and '-' not in numero_sem_formatar:
        # adicionar '-' ao número
        numero_formatado.insert(4, '-')

    elif len(numero_sem_formatar) == 7 and '-' not in numero_sem_formatar:
        # adicionar o '-' e 3 ao número
        numero_formatado.insert(0, '3')
        numero_formatado.insert(4, '-')
        mensagem = 'Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.\n'

    else:
        return 'Número inválido!'

    numero_sem_formatar = [d for d in numero_formatado if d != '-']
    mensagem += f'Telefone corrigido sem formatação: {''.join(
        numero_sem_formatar)} \nTelefone corrigido com formatação: {''.join(numero_formatado)}'

    return mensagem


print('--- VALIDA E CORRIGE NÚMERO DE TELEFONE ---')
telefone: str = input('Telefone fixo: ')
print(f'\n{formatar_numero(telefone)}')
