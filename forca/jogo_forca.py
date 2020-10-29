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
        self.__pontuacao = Pontuacao("advinhacao", self.__propriedades['pontos_iniciais'])

        tentativas = self.__propriedades['tentativas']
        print(self.__textos["interacoes"].format(tentativas, self.__forca.numero_de, self.__forca.numero_ate))

        for i in range(0, tentativas):
            print(self.__textos["diferenca_tentativa"].format(i + 1, tentativas))
            valor_tentativa = int(input(self.__textos["informe_numero"]))
            self.acertou = self.__forca.jogo(valor_tentativa)

            if self.acertou:
                break
            else:
                print(self.__textos["tente_novamente"].format(self.__textos["diferenca_" + self.__forca.texto_perdeu]))
                self.__pontuacao.perdeu_pontos(self.__propriedades['pontos_decremento'])

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
