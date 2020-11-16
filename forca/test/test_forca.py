from unittest import TestCase

from forca.forca import Forca


class TestForca(TestCase):


    def setUp(self):
        self.palavra_teste = {"palavra": "banana", "tipo": "fruta", "dica": "Fruta", "nivel": 1}
        self.forca = Forca(self.palavra_teste)

    def test_dica_da_palavra(self):
        self.assertEqual(self.forca.dica, self.palavra_teste["dica"].upper())

    def test_acertar_letra(self):
        teste = self.forca.jogo("a")
        self.assertEqual(teste, True)

    def test_errar_letra(self):
        teste = self.forca.jogo("q")
        self.assertEqual(teste, False)

    def test_informar_uma_letra_duas_vezes(self):
        teste = self.forca.jogo("a")
        teste = self.forca.jogo("a")
        self.assertEqual(teste, False)
