from advinhacao import advinhacao


def main():
    print("****************************")
    print("****** JOGO EM PYTHON ******")
    print("****************************")

    jogo = int(input("Jogos:\n1 adivinhação\n"
                      "2 forca\n"
                      "\n"
                      "Escolha o jogo:"))

    if jogo == 1:
        advinhacao()
    else:
        print("O jogo de forca ainda não foi implementado.")


if __name__ == "__main__":
    main()
