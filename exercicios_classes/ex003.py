'''
Classe Retangulo: Crie uma classe que modele um retangulo:
    Atributos: 
        LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    Métodos: 
        Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''


from math import sqrt


class Retangulo:
    def __init__(self, base: float | int, altura: float | int) -> None:
        self.base = base
        self.altura = altura

    def alterarBase(self, novo_valor: float | int) -> None:
        if novo_valor > 0:
            self.base = novo_valor

    def alterarAltura(self, novo_valor: float | int) -> None:
        if novo_valor > 0:
            self.altura = novo_valor

    def calcularArea(self) -> float:
        area = (self.base * self.altura) / 2
        return area
    
    def calcularPerimetro(self) -> float:
        lado1 = self.base
        lado2 = self.altura
        lado3 = sqrt(self.base**2 + self.altura**2)
        
        perimetro = lado1 + lado2 + lado3
        return perimetro
