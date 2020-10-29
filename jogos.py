from pontuacao.pontuacao import Pontuacao
from pathlib import Path
import json
import importlib

class Jogos:

    def __init__(self, nome_jogo, nome_modulo, nome_classe):
        module = importlib.import_module(nome_modulo)
        self.__classe = getattr(module, nome_classe)
        self.__nome_jogo = nome_jogo

        self.__carrega_textos()
        self.__instancia = self.__classe()

    def jogar(self):
        self.__instancia.introducao()
        self.__pontuacao = Pontuacao(self.__nome_jogo, 0)

        quero_jogar = True
        while quero_jogar:
            self.__instancia.interacao()
            self.__pontuacao.acumula_pontos(self.__instancia.pontuacao_rodada())
            self.__instancia.mensagem_final()
            print(self.__textos["pontos_rodada"].format(self.__instancia.pontuacao_rodada()))
            print(self.__textos["pontos_acumulados"].format(self.__pontuacao.pontuacao_geral()))
            quero_jogar = self.__quero_jogar()
            print(self.__textos["espacamento"])

        print(self.__textos["fim"])

    def __quero_jogar(self):
        return input(self.__textos["quero_jogar"]).lower() in "s1"

    def __carrega_textos(self):
        file_json = str(Path(__file__).parent.absolute()) + '/dicionario.json'
        self.__textos = json.load(open(file_json))
