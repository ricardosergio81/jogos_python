from jogos import Jogos
import os

def main():
    print("****************************")
    print("****** JOGO EM PYTHON ******")
    print("****************************")

    quero_jogar = True
    while quero_jogar:
        try:
            jogo = int(input("Lista de Jogos:\n"
                             "1 Pontuações\n"
                             "2 Adivinhação\n"
                             "3 Forca\n"
                             "4 Pedra, Papel e Tesoura\n"
                             "5 Mega Sena\n"
                             "9 Sair\n"
                             "\n"
                              "Escolha o jogo:"))

            if jogo == 2:
                jogos = Jogos("adivinhacao", "adivinhacao.jogo_adivinhacao", "JogoAdvinhacao")
                jogos.jogar()
            elif jogo == 3:
                jogos = Jogos("forca", "forca.jogo_forca", "JogoForca")
                jogos.jogar()
            elif jogo == 9:
                quero_jogar = False
            else:
                print("\n***** Jogo não implementado *****\n")
        except ValueError:
            print("\n***** Entrada Inválida *****\n")


if __name__ == "__main__":
    main()
