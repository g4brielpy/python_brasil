'''
Classe Bichinho Virtual:
    Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: 
    Nome, Fome, Saúde e Idade. OK

Métodos: 
    Alterar Nome, OK
    Fome, 
    Saúde e Idade; 
    Retornar (Nome, Fome, Saúde e Idade)

Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''


class BichinhoVirtual:
    _lista_fomes: list = ['Muita fome', 'Com fome',
                          'Satisfeito', 'Muito satisfeito']

    _lista_saude: list = ['Mal', 'Normal', 'Bem']

    def __init__(self, nome: str, fome: int, saude: int, idade: int) -> None:
        self.nome: str = nome
        self.fome: int = fome
        self.saude: int = saude
        self.idade: int = idade

    def alterarNome(self, novo_nome: str) -> str:
        if novo_nome:
            if novo_nome != self.nome:
                self.nome = novo_nome

                return 'Nome alterado com sucesso!'
            return 'Nome igual ao anterior!'
        return 'Nome inválido!'

    def alterarFome(self, fome: int) -> str:
        if fome >= 0 and fome <= 10:
            self.fome = fome

            return 'Fome alterada!'
        return 'Valor inválido!'

    def alterarSaude(self, saude: int) -> str:
        if saude >= 0 and saude <= 10:
            self.saude = saude

            return 'Saúde alterada com sucesso!'
        return 'Saúde inválida!'

    def alterarIdade(self, nova_idade: int) -> str:
        if nova_idade > 0:
            self.idade = nova_idade

            return 'Idade alterada com sucesso!'
        return 'Valor inválido!'

    def get_nome(self) -> str:
        return self.nome

    def get_fome(self) -> int:
        return self.fome

    def get_saude(self) -> int:
        return self.saude

    def get_idade(self) -> int:
        return self.idade
