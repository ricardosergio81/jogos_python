from adivinhacao.adivinhacao import Advinhacao
from adivinhacao import dicionario, propriedades
from jogo.jogo import Jogo
from pontuacao.pontuacaojogos import PontuacaoJogos
from adivinhacao.adivinhacao_error import *


class JogoAdvinhacao(Jogo):

    def __init__(self):
        self.__textos = dicionario
        self.__arquivo_propriedades = propriedades
        self.__acertou = False
        self.__pontuacao = PontuacaoJogos("advinhacao")

    def introducao(self):
        print(self.__textos.introducao)

    def interacao(self):
        self.__propriedades_niveis()

        advinhacao = Advinhacao(self.__propriedades["numero_de"], self.__propriedades["numero_ate"])
        self.__pontuacao.pontos_iniciais(self.__propriedades['pontos_iniciais'])

        tentativas = self.__propriedades['tentativas']
        print(self.__textos.interacoes.format(tentativas, advinhacao.numero_de, advinhacao.numero_ate))

        for i in range(0, tentativas):
            try:
                print(self.__textos.diferenca_tentativa.format(i + 1, tentativas))
                valor_tentativa = int(input(self.__textos.informe_numero))
                self.__acertou = advinhacao == valor_tentativa

                if self.__acertou:
                    break

            except PerdeuMenorError:
                self.__errou_tentativa(self.__textos.diferenca_menor)
            except PerdeuMaiorError:
                self.__errou_tentativa(self.__textos.diferenca_maior)
            except JaAcertouAnteriormente:
                print(self.__textos.ja_acertou)
            except ValueError:
                print("\n***** Entrada Inválida *****\n")

    def __errou_tentativa(self, mensagem):
        print(self.__textos.tente_novamente.format(mensagem))
        self.__pontuacao.perdeu_pontos(self.__propriedades['pontos_decremento'])

    def pontuacao_rodada(self):
        return self.__pontuacao.pontuacao_rodada()

    def mensagem_final(self):
        print(self.__textos.espacamento)
        if self.__acertou:
            print(self.__textos.mensagem_final_acertou)
        else:
            print(self.__textos.mensagem_final_errou)

    def __propriedades_niveis(self):
        nivel = int(input(self.__textos.introducao_nivel))
        self.__propriedades = self.__arquivo_propriedades.niveis['nivel' + str(nivel)]
