from pathlib import Path
import json
import os


class Pontuacao:

    def _carrega_pontuacao(self, jogo):
        file_json = str(Path(__file__).parent.absolute()) + "/jogos/" + jogo + ".json"
        if os.path.isfile(file_json) and os.access(file_json, os.R_OK):
            return json.load(open(file_json))

        return {"pontos": 0, "total_rodadas": 5, "rodada_atual": -1, "ultima_rodada": [0, 0, 0, 0, 0]}

    def _grava_pontuacao(self, jogo, dados):
        file_json = str(Path(__file__).parent.absolute()) + "/jogos/" + jogo + ".json"
        with open(file_json, 'w') as outfile:
            json.dump(dados, outfile)
