'''
Classe Bola: Crie uma classe que modele uma bola:
    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
'''


class Bola:
    def __init__(self, cor: str, circunferencia: str, material: str) -> None:
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self, nova_cor: str) -> None:
        if nova_cor:
            self.cor = nova_cor

    def mostrarCor(self) -> str:
        return self.cor
