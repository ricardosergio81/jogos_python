import random


class Advinhacao:

    def __init__(self, numero_de, numero_ate):
        self.__numero_de = numero_de
        self.__numero_ate = numero_ate
        self.__sorteado = self.__sorteia_numero()
        self.__ganhou = False
        self.__texto_perdeu = ""

    def jogo(self, valor_tentativa):
        resultado = False
        if valor_tentativa == self.__sorteado:
            resultado = True
        elif valor_tentativa > self.__sorteado:
            self.__texto_perdeu = "menor"
        else:
            self.__texto_perdeu = "maior"

        return resultado

    @property
    def texto_perdeu(self):
        return self.__texto_perdeu

    @property
    def numero_de(self):
        return self.__numero_de

    @property
    def numero_ate(self):
        return self.__numero_ate

    def __sorteia_numero(self):
        return random.randrange(self.__numero_de, (self.__numero_ate + 1))
