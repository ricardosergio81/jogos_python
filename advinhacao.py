import random


def advinhacao():
    tentativas = 30
    numero_de = 0
    numero_ate = 10
    acertou = False

    print("****************************")
    print("**** JOGO DE ADVINHAÇÃO ****")
    print("****************************")

    nivel = int(input("Dificuldade:\n1 fácil\n"
                      "2 médio\n"
                      "3 dificil\n"
                      "Escolha o nível:"))

    tentativas = int(tentativas / nivel)

    print("Você tera {} tentativas para acertar o número entre {} e {}".format(tentativas, numero_de, numero_ate))

    sorteado = random.randrange(numero_de, (numero_ate + 1))

    for i in range(0, tentativas):

        print("Tentativa {} de {}".format(i + 1, tentativas))
        valor_tentativa = int(input("Informe um número:"))

        if valor_tentativa == sorteado:
            print("****************************")
            print("Parabéns\nVocê acertou!")
            acertou = True
            break
        elif valor_tentativa > sorteado:
            print("Você errou.\nO número é MENOR! Tente novamente.")
        else:
            print("Você errou.\nO número é MAIOR! Tente novamente.")

    if not acertou:
        print("****************************")
        print("Que pena, você não acertou o número.\nTente novamente, quem sabe na próxima não acerte.")


if __name__ == "__main__":
    advinhacao()
