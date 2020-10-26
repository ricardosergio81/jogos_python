from pathlib import Path
import random
import json

class Advinhacao:

    def __init__(self):
        self.__introducao()
        nivel = self.__introducao_nivel()
        self.__carrega_propriedades(nivel)
        self.__numero_de = self.__propriedades["numero_de"]
        self.__numero_ate = self.__propriedades["numero_ate"]

    def jogar(self):

        self.__pontos = self.__pontos()

        self.__sorteado = self.__sorteia_numero()

        acertou = self.__interacoes()

        self.__mensagem_final(acertou)

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
            self.__pontos -= self.__pontos_decremento()
        return acertou

    def __sorteia_numero(self):
        return random.randrange(self.__numero_de, (self.__numero_ate + 1))

    def __mensagem_final(self, acertou):
        print("****************************")
        if acertou:
            print("Que pena, você não acertou o número.\nTente novamente, quem sabe na próxima não acerte.")
        else:
            print("Parabéns\nVocê acertou!\nTente a sorte novamente!")

        print("Você fez {} pontos nessa rodada.".format(self.__pontos))

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

    def __carrega_propriedades(self,nivel):
        file_json = str(Path(__file__).parent.absolute()) + '/propriedades.json'
        propriedades = json.load(open(file_json))
        self.__propriedades = propriedades['niveis']['nivel' + str(nivel)]

    def __pontos(self):
        return self.__propriedades['pontos_iniciais']

    def __pontos_decremento(self):
        return self.__propriedades['pontos_decremento']

if __name__ == "__main__":
    advinhacao = Advinhacao()
    advinhacao.jogar()
