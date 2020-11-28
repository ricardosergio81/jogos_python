from pathlib import Path
import json
import os


class Pontuacao:

	def __init__(self, jogo):
		self.__diretorio = str(Path(__file__).parent.absolute()) + "/jogos/"
		self.__arquivo_json = self.__diretorio + jogo + ".json"

	def _carrega_pontuacao(self):
		if os.path.isfile(self.__arquivo_json) and os.access(self.__arquivo_json, os.R_OK):
			return json.load(open(self.__arquivo_json))

		return {"pontos": 0, "total_rodadas": 5, "rodada_atual": -1, "ultima_rodada": [0, 0, 0, 0, 0]}

	def _grava_pontuacao(self, jogo, dados):
		if not os.path.isdir(self.__diretorio):
			os.mkdir(self.__diretorio)

		with open(self.__arquivo_json, 'w') as outfile:
			json.dump(dados, outfile)
