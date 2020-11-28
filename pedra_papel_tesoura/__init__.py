from carrega_json import *

dicionario = carrega_json_dict(__file__, 'dicionario.json')

propriedades = carrega_json_list(__file__, 'propriedades.json')

from .jogo_pedra_papel_tesoura import JogoPedraPapelTesoura
