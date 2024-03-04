'''
Classe Conta Corrente: 
    Crie uma classe para implementar uma conta corrente. 

    A classe deve possuir os seguintes atributos: 
        número da conta, 
        nome do correntista, 
        saldo. 

    Os métodos são os seguintes: 
        alterarNome, 
        depósito, 
        saque (opcional); 
    
    No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios
'''


class ContaCorrente:
    def __init__(self, numero_conta: int, nome_correntista: str, saldo: float = 0.0) -> None:
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome: str) -> None:
        if novo_nome:
            self.nome_correntista = novo_nome

    def deposito(self, valor_deposito: float) -> None:
        if valor_deposito > 0:
            self.saldo += valor_deposito

    def saque(self, valor_saque: float) -> None:
        if valor_saque > 0 and valor_saque < self.saldo:
            self.saldo -= valor_saque
