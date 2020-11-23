from sorteio.numeros import Numeros
from adivinhacao.adivinhacao_error import *


class Advinhacao:

    def __init__(self, numero_de, numero_ate):
        self.__numero_de = numero_de
        self.__numero_ate = numero_ate
        self.__sorteado = self.__sorteia_numero()
        self.__acertou = False

    def __eq__(self, valor_tentativa):
        if not self.__acertou:
            if valor_tentativa > self.__sorteado:
                raise PerdeuMenorError
            elif valor_tentativa < self.__sorteado:
                raise PerdeuMaiorError
            self.__acertou = True
            return True
        else:
            raise JaAcertouAnteriormente

    @property
    def acertou(self):
        return self.__acertou

    @property
    def numero_de(self):
        return self.__numero_de

    @property
    def numero_ate(self):
        return self.__numero_ate

    def __sorteia_numero(self):
        sorteia = Numeros()
        sorteia.numero_de = self.__numero_de
        sorteia.numero_ate = self.numero_ate
        return sorteia.sortear()
