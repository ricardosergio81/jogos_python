from pathlib import Path
import random
import json

class Advinhacao:

    def __init__(self):
        self.__pontos_geral = 0

    def jogar(self):
        self.__introducao()
        self.__carrega_propriedades()
        quero_jogar = True
        while quero_jogar:
            nivel = self.__introducao_nivel()
            self.__propriedades_niveis(nivel)
            self.__numero_de = self.__propriedades["numero_de"]
            self.__numero_ate = self.__propriedades["numero_ate"]
            self.__pontos = self.__propriedades['pontos_iniciais']
            self.__sorteado = self.__sorteia_numero()

            acertou = self.__interacoes()

            self.__mensagem_final(acertou)
            quero_jogar = self.__quero_jogar()
            print("****************************")

        print("******** ATÉ MAIS **********")
        print("****************************")
    def __interacoes(self):
        tentativas = self.__marca_tentativas()
        acertou = False
        print("Você tera {} tentativas para acertar o número entre {} e {}".format(tentativas, self.__numero_de,
                                                                                   self.__numero_ate))
        for i in range(0, tentativas):
            diferenca ="MAIOR"
            print("Tentativa {} de {}".format(i + 1, tentativas))
            valor_tentativa = int(input("Informe um número:"))

            if valor_tentativa == self.__sorteado:
                acertou = True
                break
            elif valor_tentativa > self.__sorteado:
                diferenca ="MENOR"

            print("Você errou.\nO número é {}! Tente novamente.".format(diferenca))
            self.__pontos -= self.__propriedades['pontos_decremento']

        return acertou

    def __sorteia_numero(self):
        return random.randrange(self.__numero_de, (self.__numero_ate + 1))

    def __mensagem_final(self, acertou):
        print("****************************")
        if acertou:
            print("Parabéns\nVocê acertou!\nTente novamente e faça mais pontos!")
        else:
            print("Que pena, você não acertou o número.\nTente novamente, quem sabe na próxima não acerte.")

        print("Você fez {} pontos nessa rodada.".format(self.__pontos))
        self.__pontos_geral += self.__pontos
        print("Você tem acumulado {} .".format(self.__pontos_geral))

    def __introducao(self):
        print("****************************")
        print("**** JOGO DE ADVINHAÇÃO ****")
        print("****************************")

    def __introducao_nivel(self):
        return int(input("Dificuldade:\n1 fácil\n"
                  "2 médio\n"
                  "3 dificil\n"
                  "Escolha o nível:"))

    def __marca_tentativas(self):
       return self.__propriedades['tentativas']

    def __carrega_propriedades(self):
        file_json = str(Path(__file__).parent.absolute()) + '/propriedades.json'
        self.__arquivo_propriedades = json.load(open(file_json))

    def __propriedades_niveis(self, nivel):
        self.__propriedades = self.__arquivo_propriedades['niveis']['nivel' + str(nivel)]

    def __quero_jogar(self):
        return input("Deseja jogar novamente?\n(S) Sim\n(N) Não").lower() == "s"


if __name__ == "__main__":
    advinhacao = Advinhacao()
    advinhacao.jogar()
