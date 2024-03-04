'''
Classe Pessoa: Crie uma classe que modele uma pessoa:
    Atributos:
        nome, idade, peso e altura
    Métodos: 
        envelhercer, 
        engordar, 
        emagrecer, 
        crescer. 

Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''


class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhercer(self):
        pass

    def engordar(self, pesos_engordar: float) -> None:
        if pesos_engordar > 0:
            self.peso += pesos_engordar

    def emagrecer(self, pesos_emagrecer: float) -> None:
        if pesos_emagrecer > 0:
            self.peso -= pesos_emagrecer

    def crescer(self, metros_cresce: float) -> None:
        if metros_cresce > 0:
            self.altura += metros_cresce
