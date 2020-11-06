from pathlib import Path
import json


def carrega_json(diretorio, file):
    file_json = str(Path(diretorio).parent.absolute()) + '/' + file
    return json.load(open(file_json))
