from pedra_papel_tesoura.enum_ppt import EnumPPT
from pedra_papel_tesoura.pedra_papel_tesoura import PedraPapelTesoura
from pedra_papel_tesoura import dicionario, propriedades
from jogo.jogo import Jogo
from pontuacao.pontuacaojogos import PontuacaoJogos
import random

class JogoPedraPapelTesoura(Jogo):

    def __init__(self):
        self.__textos = dicionario
        self.__propriedades = propriedades
        self.__valor_tentativa = ""

    def introducao(self):
        print(self.__textos.introducao)

    def interacao(self):
        self.__pedra_papel_tesoura = PedraPapelTesoura(self.__sorteia())
        self.__pontuacao = PontuacaoJogos("pedra_papel_tesoura", self.__propriedades['pontos_iniciais'])

        total_de_tentativas = self.__propriedades['tentativas']
        print(self.__textos.interacoes.format(total_de_tentativas))

        try:
            self.__valor_tentativa = int(input(self.__textos.informe_entrada))
            self.acertou = self.__pedra_papel_tesoura.jogo(self.__valor_tentativa)

            if not self.acertou:
                self.__pontuacao.perdeu_pontos(self.__propriedades['pontos_decremento'])

        except ValueError as erro:
            print(erro)

    def pontuacao_rodada(self):
        return self.__pontuacao.pontuacao_rodada()

    def mensagem_final(self):
        print(self.__textos.espacamento)
        if self.acertou:
            print(self.__textos.mensagem_final_acertou.format(self.__pedra_papel_tesoura.valor_sorteado().name, EnumPPT(self.__valor_tentativa).name))
        else:
            print(self.__textos.mensagem_final_errou.format(self.__pedra_papel_tesoura.valor_sorteado().name, EnumPPT(self.__valor_tentativa).name))

    def __propriedades_niveis(self, nivel):
        self.__propriedades = self.__arquivo_propriedades.niveis['nivel' + str(nivel)]

    def __sorteia(self):
       return random.choice(list(EnumPPT))

