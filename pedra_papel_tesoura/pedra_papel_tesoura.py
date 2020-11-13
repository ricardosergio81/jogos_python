

class PedraPapelTesoura:

    def __init__(self):
        self.__texto_perdeu = ""

    def jogo(self, valor_tentativa):
        resultado = False
        self.__texto_perdeu = "letra_informada"

        if self.letras_testadas(valor_tentativa.upper()):
            resultado = valor_tentativa.upper() in self.__palavra
            self.__texto_perdeu = "acertou"
            self.marca_letra_palavra(valor_tentativa)

        return resultado

