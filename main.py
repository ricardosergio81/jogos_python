from jogos import Jogos
from adivinhacao.jogo_adivinhacao import JogoAdvinhacao

def main():
    print("****************************")
    print("****** JOGO EM PYTHON ******")
    print("****************************")

    jogo = int(input("Jogos:\n1 adivinhação\n"
                      "2 forca\n"
                      "\n"
                      "Escolha o jogo:"))

    if jogo == 1:
        jogos = Jogos("adivinhacao", "adivinhacao.jogo_adivinhacao", "JogoAdvinhacao")
        jogos.jogar()
    else:
        print("O jogo de forca ainda não foi implementado.")


if __name__ == "__main__":
    main()
