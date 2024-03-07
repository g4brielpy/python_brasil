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

    def __init__(self, nome: str, fome: str, saude: str, idade: int) -> None:
        self.nome: str = nome
        self.fome: str = fome if fome in BichinhoVirtual._lista_fomes else 'Satisfeito'
        self.saude: str = saude
        self.idade: int = idade

    def alterarNome(self, novo_nome: str) -> str:
        if novo_nome:
            if novo_nome != self.nome:
                self.nome = novo_nome

                return 'Nome alterado com sucesso!'
            return 'Nome igual ao anterior!'
        return 'Nome inválido!'

    def alterarFome(self, fome: str) -> str:
        if fome and fome in BichinhoVirtual._lista_fomes:
            self.fome = fome

            return 'Fome alterada!'
        return 'Valor inválido!'
