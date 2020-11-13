import random
from sorteio.sorteio import Sorteio
from carrega_json import carrega_json


class Paravras(Sorteio):

    def __init__(self):
        self.nivel = 0
        self.tipo = False
        self.__carragar_palavras()

    def sortear(self):
        random_index = random.randrange(0, len(self.__lista_palavras))
        return self.__lista_palavras[random_index]

    def __carragar_palavras(self):
        self.__lista_palavras = carrega_json(__file__, 'lista_palavras.json')
