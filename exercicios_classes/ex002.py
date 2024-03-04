'''
Classe Quadrado: Crie uma classe que modele um quadrado:
    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''


class Quadrado:
    def __init__(self, tamanho_lados: float | int) -> None:
        self.tamanho_lados = tamanho_lados

    def alterarLados(self, novo_valor: float | int) -> None:
        if novo_valor:
            self.tamanho_lados = novo_valor

    def exibirLados(self) -> int | float:
        return self.tamanho_lados

    def calcularArea(self) -> float:
        area = self.tamanho_lados ** 2
        return area
