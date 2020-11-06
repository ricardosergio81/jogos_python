from carrega_json import carrega_json

dicionario = carrega_json(__file__, 'dicionario.json')

propriedades = carrega_json(__file__, 'propriedades.json')

from .jogo_adivinhacao import JogoAdvinhacao
