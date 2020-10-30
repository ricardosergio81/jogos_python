from jogos import Jogos

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
        jogos = Jogos("forca", "forca.jogo_forca", "JogoForca")
        jogos.jogar()


if __name__ == "__main__":
    main()
