from forca.forca import Forca
from pontuacao.pontuacao import Pontuacao
from pathlib import Path
import json


class JogoForca():

    def __init__(self):
        self.__carrega_textos()
        self.__carrega_propriedades()

    def introducao(self):
        print(self.__textos["introducao"])

    def interacao(self):
        nivel = int(input(self.__textos["introducao_nivel"]))
        self.__propriedades_niveis(nivel)

        self.__forca = Forca()
        self.__pontuacao = Pontuacao("forca", self.__propriedades['pontos_iniciais'])

        total_de_tentativas = self.__propriedades['tentativas']
        print(self.__textos["interacoes"].format(total_de_tentativas))
        print(self.__forca.palavra_oculta)

        fim_de_jogo = False
        tentativa = 1
        while not fim_de_jogo:
            print(self.__textos["diferenca_tentativa"].format(tentativa, total_de_tentativas))
            valor_tentativa = input(self.__textos["informe_entrada"])
            self.acertou = self.__forca.jogo(valor_tentativa)

            if not self.acertou:
                self.__pontuacao.perdeu_pontos(self.__propriedades['pontos_decremento'])

            print(self.__textos[self.__forca.texto_perdeu])
            print(self.__forca.palavra_oculta)

            fim_de_jogo = (not self.__forca.acertou_palavra) | tentativa >= total_de_tentativas
            tentativa += 1


    def pontuacao_rodada(self):
        return self.__pontuacao.pontuacao_rodada()

    def mensagem_final(self):
        print(self.__textos["espacamento"])
        if self.acertou:
            print(self.__textos["mensagem_final_acertou"])
        else:
            print(self.__textos["mensagem_final_errou"])

    def __carrega_propriedades(self):
        file_json = str(Path(__file__).parent.absolute()) + '/propriedades.json'
        self.__arquivo_propriedades = json.load(open(file_json))

    def __propriedades_niveis(self, nivel):
        self.__propriedades = self.__arquivo_propriedades['niveis']['nivel' + str(nivel)]

    def __carrega_textos(self):
        file_json = str(Path(__file__).parent.absolute()) + '/dicionario.json'
        self.__textos = json.load(open(file_json))
