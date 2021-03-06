#! /usr/bin/python3

from jogo.jogos import Jogos
from pontuacao.pontuacaogeral import PontuacaoGeral

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

            if jogo == 1:
                PontuacaoGeral().rodar()
            elif jogo == 2:
                Jogos("adivinhacao", "adivinhacao.jogo_adivinhacao", "JogoAdvinhacao").rodar()
            elif jogo == 3:
                Jogos("forca", "forca.jogo_forca", "JogoForca").rodar()
            elif jogo == 4:
                Jogos("pedra_papel_tesoura", "pedra_papel_tesoura.jogo_pedra_papel_tesoura", "JogoPedraPapelTesoura").rodar()
            elif jogo == 9:
                print("\n\nFim de jogo.\nAté Mais (: ")
                quero_jogar = False
            else:
                print("\n***** Jogo não implementado *****\n")
        except ValueError:
            print("\n***** Entrada Inválida *****\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt):
        print("\n\nFim de jogo.\nAté Mais (: ")
