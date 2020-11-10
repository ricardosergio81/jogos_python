from pathlib import Path
import json
import random
from carrega_json import carrega_json


class Forca:

    def __init__(self, nivel):
        self.__sorteado = self.__sorteia(nivel)
        self.__letras_testadas = ""
        self.__texto_perdeu = ""
        self.__palavra = self.__sorteado['palavra'].upper()
        self.__palavra_oculta = self.__ocultar_palavra(self.__palavra)

    def jogo(self, valor_tentativa):
        resultado = False
        self.__texto_perdeu = "letra_informada"

        if self.letras_testadas(valor_tentativa.upper()):
            resultado = valor_tentativa.upper() in self.__palavra
            self.__texto_perdeu = "acertou"
            self.marca_letra_palavra(valor_tentativa)

        return resultado

    def letras_testadas(self, valor_tentativa):
        if valor_tentativa in self.__letras_testadas:
            return False
        else:
            self.__letras_testadas = self.__letras_testadas + valor_tentativa
            return True

    def marca_letra_palavra(self, valor_tentativa):
        index = 0
        for letra in self.__palavra:
            if (valor_tentativa.upper() == letra.upper()):
                self.__palavra_oculta[index] = letra
            index += 1

    @property
    def dica(self):
        return self.__sorteado['dica'].upper()

    @property
    def palavra_oculta(self):
        return self.__palavra_oculta

    def __ocultar_palavra(self, palavra):
        return ["_" for letra in palavra]

    @property
    def acertou_palavra(self):
        return "_" in self.__palavra_oculta

    @property
    def texto_perdeu(self):
        return self.__texto_perdeu

    def __sorteia(self, nivel):
           lista_palavras = carrega_json(__file__, 'lista_palavras.json')
           random_index = random.randrange(0, len(lista_palavras['nivel' + str(nivel)]))
           return lista_palavras['nivel' + str(nivel)][random_index]

