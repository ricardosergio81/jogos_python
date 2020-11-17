from carrega_json import carrega_json_dict

dicionario = carrega_json_dict(__file__, 'dicionario.json')

propriedades = carrega_json_dict(__file__, 'propriedades.json')

from .jogo_forca import JogoForca
