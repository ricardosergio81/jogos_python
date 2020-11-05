from pathlib import Path
import json

file_json = str(Path(__file__).parent.absolute()) + '/dicionario.json'
dicionario = json.load(open(file_json))

file_json = str(Path(__file__).parent.absolute()) + '/propriedades.json'
propriedades = json.load(open(file_json))

from .jogo_forca import JogoForca
