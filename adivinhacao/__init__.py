from carrega_json import carrega_json_dict, carrega_json_list

dicionario = carrega_json_dict(__file__, 'dicionario.json')

propriedades = carrega_json_dict(__file__, 'propriedades.json')

from .jogo_adivinhacao import JogoAdvinhacao
