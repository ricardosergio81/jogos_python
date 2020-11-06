from jogos import Jogos

def main():
    print("****************************")
    print("****** JOGO EM PYTHON ******")
    print("****************************")

    jogo = int(input("Jogos:\n1 Adivinhação\n"
                      "2 Forca\n"
                     "3 Pedra, Papel e Tesoura\n"
                     "4 Mega Sena\n"
                      "\n"
                      "Escolha o jogo:"))

    if jogo == 1:
        jogos = Jogos("adivinhacao", "adivinhacao.jogo_adivinhacao", "JogoAdvinhacao")
        jogos.jogar()
    elif jogo == 2:
        jogos = Jogos("forca", "forca.jogo_forca", "JogoForca")
        jogos.jogar()
    else:
        print("Jogo não implementado")


if __name__ == "__main__":
    main()
