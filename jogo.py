import abc


class Jogo:

    @abc.abstractmethod
    def introducao(self):
        pass

    @abc.abstractmethod
    def pontuacao_rodada(self):
        pass

    @abc.abstractmethod
    def interacao(self):
        pass

    @abc.abstractmethod
    def mensagem_final(self):
        pass
