'''
Classe TV: 
    Faça um programa que simule um televisor criando-o como um objeto. 
    O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
    Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''


class TV:
    def __init__(self, numeros_canais: int, volume: int = 5, canal: int = 1) -> None:
        self.numeros_canais: int = numeros_canais
        self.volume: int = volume
        self.canal: int = canal

    def trocarCanal(self, canal_trocar: int) -> str:
        if canal_trocar:
            if canal_trocar > 0 and canal_trocar <= self.numeros_canais:
                self.canal = canal_trocar

                return 'Canal alterado!'
        return 'Canal inválido!'

    def alterarVolume(self, volume_novo: int) -> str:
        if volume_novo and type(volume_novo) == int:
            mensagem: str = 'Volume aumentado' if volume_novo > self.volume else 'Volume abaixado'
            self.volume = volume_novo

            return mensagem
        return 'Valor inválido'
