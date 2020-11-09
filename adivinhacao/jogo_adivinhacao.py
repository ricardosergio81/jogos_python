from adivinhacao.adivinhacao import Advinhacao
from adivinhacao import dicionario, propriedades
from pontuacao.pontuacao import Pontuacao


class JogoAdvinhacao():

    def __init__(self):
        self.__textos = dicionario
        self.__arquivo_propriedades = propriedades

    def introducao(self):
        print(self.__textos["introducao"])

    def interacao(self):
        nivel = int(input(self.__textos["introducao_nivel"]))
        self.__propriedades_niveis(nivel)

        self.__advinhacao = Advinhacao(self.__propriedades["numero_de"], self.__propriedades["numero_ate"])
        self.__pontuacao = Pontuacao("advinhacao", self.__propriedades['pontos_iniciais'])

        tentativas = self.__propriedades['tentativas']
        print(self.__textos["interacoes"].format(tentativas, self.__advinhacao.numero_de, self.__advinhacao.numero_ate))

        for i in range(0, tentativas):
            try:
                print(self.__textos["diferenca_tentativa"].format(i + 1, tentativas))
                valor_tentativa = int(input(self.__textos["informe_numero"]))
                self.acertou = self.__advinhacao.jogo(valor_tentativa)

                if self.acertou:
                    break
                else:
                    print(self.__textos["tente_novamente"].format(self.__textos["diferenca_"+self.__advinhacao.texto_perdeu]))
                    self.__pontuacao.perdeu_pontos(self.__propriedades['pontos_decremento'])

            except ValueError:
                print("\n***** Entrada Inválida *****\n")

    def pontuacao_rodada(self):
        return self.__pontuacao.pontuacao_rodada()

    def mensagem_final(self):
        print(self.__textos["espacamento"])
        if self.acertou:
            print(self.__textos["mensagem_final_acertou"])
        else:
            print(self.__textos["mensagem_final_errou"])

    def __propriedades_niveis(self, nivel):
        self.__propriedades = self.__arquivo_propriedades['niveis']['nivel' + str(nivel)]
