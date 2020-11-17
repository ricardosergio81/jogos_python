from pathlib import Path
import json


class carrega_json_dict(dict):
    def __init__(self, diretorio, file):
        file_json = str(Path(diretorio).parent.absolute()) + '/' + file
        self.__dict__ = json.load(open(file_json))


def carrega_json_list(diretorio, file):
    file_json = str(Path(diretorio).parent.absolute()) + '/' + file
    return json.load(open(file_json))
