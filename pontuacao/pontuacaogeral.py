from pontuacao.pontuacao import Pontuacao
from pathlib import Path
import os


class PontuacaoGeral():

    def __init__(self):
        self.__diretorio = str(Path(__file__).parent.absolute()) + "/jogos/"    

    def rodar(self):
    	for diretorio, nomediretorio, nomearquivos in os.walk(self.__diretorio):
        	for nomearquivo in nomearquivos:
        		(arquivo, ext) = os.path.splitext(nomearquivo)
        		pontuacao = Pontuacao(arquivo)._carrega_pontuacao()
        		print("Pontuação Total no jogo {}: {}".format( arquivo, str(pontuacao["pontos"])))








