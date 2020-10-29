from pathlib import Path
import json
import os

class Pontuacao:

    def __init__(self, jogo, pontuacao):
        self.__jogo = jogo
        self.__pontuacao = pontuacao
        self.__carrega_pontuacao_geral()

    def ganhou_pontos(self, pontos):
        self.__pontuacao += pontos

    def perdeu_pontos(self, pontos):
        self.__pontuacao -= pontos

    def pontuacao_rodada(self):
        return self.__pontuacao

    def acumula_pontos(self, pontos):
        self.__pontuacao_geral["pontos"] += pontos
        self.__grava_pontuacao_geral()

    def pontuacao_geral(self):
        return self.__pontuacao_geral["pontos"]

    def __carrega_pontuacao_geral(self):
        file_json = str(Path(__file__).parent.absolute()) + "/jogos/" + self.__jogo + ".json"
        if os.path.isfile(file_json) and os.access(file_json, os.R_OK):
            self.__pontuacao_geral = json.load(open(file_json))
        else:
            self.__pontuacao_geral = {"pontos": 0}

    def __grava_pontuacao_geral(self):
        file_json = str(Path(__file__).parent.absolute()) + "/jogos/" + self.__jogo + ".json"
        with open(file_json, 'w') as outfile:
            json.dump(self.__pontuacao_geral, outfile)
