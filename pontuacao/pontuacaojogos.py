from pontuacao.pontuacao import Pontuacao


class PontuacaoJogos(Pontuacao):

    def __init__(self, jogo, pontuacao):
        super().__init__()
        self.__jogo = jogo
        self.__pontuacao = pontuacao
        self.__pontuacao_geral = self._carrega_pontuacao(jogo)
        self.__rodada_atual = self.marca_rodada_atual(self.__pontuacao_geral['rodada_atual'], self.__pontuacao_geral['total_rodadas'])

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
        if rodada_atual == -1 or rodada_atual == total_rodadas:
            return 0
        else:
            print(rodada_atual)
            return rodada_atual + 1





