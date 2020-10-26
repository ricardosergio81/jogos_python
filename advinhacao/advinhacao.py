from pathlib import Path
import random
import json

class Advinhacao:

    def __init__(self):
        self.__carrega_propriedades()
        self.__numero_de = self.__propriedades["numero_de"]
        self.__numero_ate = self.__propriedades["numero_ate"]

    def jogar(self):
        acertou = False

        self.__introducao()

        self.__nivel = self.__introducao_nivel()

        tentativas = self.__marca_tentativas()

        print("Você tera {} tentativas para acertar o número entre {} e {}".format(tentativas, self.__numero_de, self.__numero_ate))

        self.__sorteado = self.__sorteia_numero()

        for i in range(0, tentativas):

            print("Tentativa {} de {}".format(i + 1, tentativas))
            valor_tentativa = int( input("Informe um número:"))

            if valor_tentativa == self.__sorteado:
                acertou = True
                break
            elif valor_tentativa > self.__sorteado:
                print("Você errou.\nO número é MENOR! Tente novamente.")
            else:
                print("Você errou.\nO número é MAIOR! Tente novamente.")

        self.__mensagem_final(acertou)

    def __sorteia_numero(self):
        return random.randrange(self.__numero_de, (self.__numero_ate + 1))

    def __mensagem_final(self, acertou):
        print("****************************")
        if acertou:
            print("Que pena, você não acertou o número.\nTente novamente, quem sabe na próxima não acerte.")
        else:
            print("Parabéns\nVocê acertou!\nTente a sorte novamente!")

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
       return self.__propriedades['niveis']['nivel' + str(self.__nivel)]

    def __carrega_propriedades(self):
        file_json = str(Path(__file__).parent.absolute()) + '/propriedades.json'
        self.__propriedades = json.load(open(file_json))


if __name__ == "__main__":
    advinhacao = Advinhacao()
    advinhacao.jogar()
