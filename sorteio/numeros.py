import abc
import random

from sorteio.sorteio import Sorteio


class Numeros(Sorteio):

    def __init__(self):
        self.__numero_de = 0
        self.__numero_ate = 1000

    @abc.abstractmethod
    def sortear(self):
        return random.randrange(self.__numero_de, (self.__numero_ate + 1))

    @property
    def numero_de(self):
        return self.__numero_de

    @numero_de.setter
    def numero_de(self, numero: int):
        self.__numero_de = numero

    @property
    def numero_ate(self):
        return self.__numero_ate

    @numero_ate.setter
    def numero_ate(self, numero: int):
        self.__numero_ate = numero

