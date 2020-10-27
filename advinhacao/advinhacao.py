import random


class Advinhacao:

    def __init__(self, numero_de, numero_ate):
        self.__numero_de = numero_de
        self.__numero_ate = numero_ate
        self.__sorteado = self.__sorteia_numero()

    def jogo(self, valor_tentativa):
        resultado = 1
        if valor_tentativa == self.__sorteado:
            resultado = 0
        elif valor_tentativa > self.__sorteado:
            resultado = -1
        return resultado

    @property
    def numero_de(self):
        return self.__numero_de

    @property
    def numero_ate(self):
        return self.__numero_ate

    def __sorteia_numero(self):
        return random.randrange(self.__numero_de, (self.__numero_ate + 1))
