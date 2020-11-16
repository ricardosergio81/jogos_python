from pedra_papel_tesoura.enum_ppt import EnumPPT

class PedraPapelTesoura:

    def __init__(self, valor_sorteado):
        self.__valor_sorteado = valor_sorteado

    def jogo(self, valor_tentativa):
        valor = EnumPPT(valor_tentativa)

        if self.__valor_sorteado == EnumPPT.PEDRA and valor == EnumPPT.PAPEL:
            return True
        elif self.__valor_sorteado == EnumPPT.PAPEL and valor == EnumPPT.TESOURA:
            return True
        elif self.__valor_sorteado == EnumPPT.TESOURA and valor == EnumPPT.PEDRA:
            return True

        return False

    def valor_sorteado(self):
        return self.__valor_sorteado