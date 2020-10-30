from pathlib import Path
import json
import random


class Forca:

    def __init__(self):
        self.__sorteado = self.__sorteia()
        self.__ganhou = False
        self.__texto_perdeu = ""

    def jogo(self, valor_tentativa):
        resultado = valor_tentativa in self.__sorteado['palavra']
        self.__texto_perdeu = "maior"
        return resultado

    def __fim_de_jogo(self):
        return False

    @property
    def texto_perdeu(self):
        return self.__texto_perdeu

    def __sorteia(self):
        file_json = str(Path(__file__).parent.absolute()) + "/lista_palavras.json"
        with open(file_json, 'r') as outfile:
           lista_palavras = json.load(outfile)
           random_index = random.randrange(0, len(lista_palavras['nivel1']) )
           return lista_palavras['nivel1'][random_index]

