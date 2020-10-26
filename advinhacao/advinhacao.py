from pathlib import Path
import random
import json

class Advinhacao:

    def __init__(self):
        self.__pontos_geral = 0
        self.__carrega_textos()
        self.__carrega_propriedades()

    def jogar(self):
        self.__introducao()
        quero_jogar = True
        while quero_jogar:
            nivel = self.__introducao_nivel()
            self.__propriedades_niveis(nivel)
            self.__numero_de = self.__propriedades["numero_de"]
            self.__numero_ate = self.__propriedades["numero_ate"]
            self.__pontos = self.__propriedades['pontos_iniciais']
            self.__sorteado = self.__sorteia_numero()

            acertou = self.__interacoes()

            self.__mensagem_final(acertou)
            quero_jogar = self.__quero_jogar()
            print(self.__textos["espacamento"])

        print(self.__textos["fim"])
        print(self.__textos["espacamento"])

    def __interacoes(self):
        tentativas = self.__marca_tentativas()
        acertou = False
        print(self.__textos["interacoes"].format(tentativas, self.__numero_de, self.__numero_ate))

        for i in range(0, tentativas):
            diferenca = self.__textos["diferenca_maior"]
            print(self.__textos["diferenca_tentativa"].format(i + 1, tentativas))
            valor_tentativa = int(input(self.__textos["informe_numero"]))

            if valor_tentativa == self.__sorteado:
                acertou = True
                break
            elif valor_tentativa > self.__sorteado:
                diferenca = self.__textos["diferenca_menor"]

            print(self.__textos["tente_novamente"].format(diferenca))
            self.__pontos -= self.__propriedades['pontos_decremento']

        return acertou

    def __sorteia_numero(self):
        return random.randrange(self.__numero_de, (self.__numero_ate + 1))

    def __mensagem_final(self, acertou):
        print(self.__textos["espacamento"])
        if acertou:
            print(self.__textos["mensagem_final_acertou"])
        else:
            print(self.__textos["mensagem_final_errou"])

        print(self.__textos["pontos_rodada"].format(self.__pontos))
        self.__pontos_geral += self.__pontos
        print(self.__textos["pontos_acumulados"].format(self.__pontos_geral))

    def __introducao(self):
        print(self.__textos["introducao"])

    def __introducao_nivel(self):
        return int(input(self.__textos["introducao_nivel"]))

    def __marca_tentativas(self):
       return self.__propriedades['tentativas']

    def __carrega_propriedades(self):
        file_json = str(Path(__file__).parent.absolute()) + '/propriedades.json'
        self.__arquivo_propriedades = json.load(open(file_json))

    def __propriedades_niveis(self, nivel):
        self.__propriedades = self.__arquivo_propriedades['niveis']['nivel' + str(nivel)]

    def __quero_jogar(self):
        return input(self.__textos["quero_jogar"]).lower() in "s1"

    def __carrega_textos(self):
        file_json = str(Path(__file__).parent.absolute()) + '/dicionario.json'
        self.__textos = json.load(open(file_json))


if __name__ == "__main__":
     Advinhacao().jogar()
