from sorteio.numeros import Numeros
from adivinhacao.adivinhacao_error import PerdeuMaiorError, PerdeuMenorError


class Advinhacao:

    def __init__(self, numero_de, numero_ate):
        self.__numero_de = numero_de
        self.__numero_ate = numero_ate
        self.__sorteado = self.__sorteia_numero()

    def jogo(self, valor_tentativa):
        if valor_tentativa > self.__sorteado:
            raise PerdeuMenorError
        elif valor_tentativa < self.__sorteado:
            raise PerdeuMaiorError

        return True

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
