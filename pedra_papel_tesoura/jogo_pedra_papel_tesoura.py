from pedra_papel_tesoura.pedra_papel_tesoura import PedraPapelTesoura
from pedra_papel_tesoura import dicionario, propriedades
from jogo import Jogo
from pontuacao.pontuacaojogos import PontuacaoJogos
from sorteio.palavras import Paravras


class JogoPedraPapelTesoura(Jogo):

    def __init__(self):
        self.__textos = dicionario
        self.__arquivo_propriedades = propriedades

    def introducao(self):
        print(self.__textos["introducao"])

    def interacao(self):
        self.__forca = PedraPapelTesoura()
        self.__pontuacao = PontuacaoJogos("pedra_papel_tesoura", self.__propriedades['pontos_iniciais'])

        total_de_tentativas = self.__propriedades['tentativas']
        print(self.__textos["interacoes"].format(total_de_tentativas))
        print(self.__forca.palavra_oculta)

        fim_de_jogo = False
        tentativa = 1
        while not fim_de_jogo:
            try:
                print(self.__textos["diferenca_tentativa"].format(tentativa, total_de_tentativas))
                valor_tentativa = input(self.__textos["informe_entrada"])
                self.acertou = self.__forca.jogo(valor_tentativa)

                if not self.acertou:
                    self.__pontuacao.perdeu_pontos(self.__propriedades['pontos_decremento'])

                print(self.__textos[self.__forca.texto_perdeu])
                print(self.__forca.palavra_oculta)

                fim_de_jogo = not (self.__forca.acertou_palavra or tentativa >= total_de_tentativas)
                tentativa += 1
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

    def __sorteia_palavra(self):
        palavras = Paravras()
        return palavras.sortear()