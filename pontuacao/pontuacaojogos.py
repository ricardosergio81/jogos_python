from pontuacao.pontuacao import Pontuacao


class PontuacaoJogos(Pontuacao):

    def __init__(self, jogo):
        super(PontuacaoJogos, self).__init__(jogo)
        self.__jogo = jogo
        self.__pontuacao = 0
        self.__pontuacao_geral = self._carrega_pontuacao()
        self.__rodada_atual = self.marca_rodada_atual(self.__pontuacao_geral['rodada_atual'], self.__pontuacao_geral['total_rodadas'])

    def pontos_iniciais(self, pontos):
        self.__pontuacao = pontos

    def ganhou_pontos(self, pontos):
        self.__pontuacao += pontos

    def perdeu_pontos(self, pontos):
        self.__pontuacao -= pontos

    def pontuacao_rodada(self):
        return self.__pontuacao

    def acumula_pontos(self, pontos):
        self.__pontuacao_geral["pontos"] += pontos
        self.__pontuacao_geral["rodada_atual"] = self.__rodada_atual
        self.__pontuacao_geral["ultima_rodada"][self.__rodada_atual] = pontos
        self._grava_pontuacao(self.__jogo, self.__pontuacao_geral)

    def pontuacao_geral(self):
        return self.__pontuacao_geral["pontos"]

    def marca_rodada_atual(self, rodada_atual, total_rodadas):
        if rodada_atual == -1 or rodada_atual == total_rodadas - 1:
            return 0
        else:
            return rodada_atual + 1





