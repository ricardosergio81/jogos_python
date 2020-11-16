from unittest import TestCase

from pedra_papel_tesoura.enum_ppt import EnumPPT
from pedra_papel_tesoura.pedra_papel_tesoura import PedraPapelTesoura


class TestPedraPapelTesoura(TestCase):

    def setUp(self):
        jogo = PedraPapelTesoura(EnumPPT.PEDRA)

    def test_jogar_pedra_contra_pedra_para_perder(self):
        jogo = PedraPapelTesoura(EnumPPT.PEDRA)
        teste = jogo.jogo(1)
        self.assertEqual(teste, False)

    def test_jogar_papel_contra_pedra_para_ganhar(self):
        jogo = PedraPapelTesoura(EnumPPT.PEDRA)
        teste = jogo.jogo(2)
        self.assertEqual(teste, True)

    def test_jogar_tesoura_contra_pedra_para_perder(self):
        jogo = PedraPapelTesoura(EnumPPT.PEDRA)
        teste = jogo.jogo(3)
        self.assertEqual(teste, False)

    def test_jogar_pedra_contra_papel_para_perder(self):
        jogo = PedraPapelTesoura(EnumPPT.PAPEL)
        teste = jogo.jogo(1)
        self.assertEqual(teste, False)

    def test_jogar_papel_contra_papel_para_peder(self):
        jogo = PedraPapelTesoura(EnumPPT.PAPEL)
        teste = jogo.jogo(2)
        self.assertEqual(teste, False)

    def test_jogar_tesoura_contra_papel_para_ganhar(self):
        jogo = PedraPapelTesoura(EnumPPT.PAPEL)
        teste = jogo.jogo(3)
        self.assertEqual(teste, True)

    def test_jogar_pedra_contra_tesoura_para_ganhar(self):
        jogo = PedraPapelTesoura(EnumPPT.TESOURA)
        teste = jogo.jogo(1)
        self.assertEqual(teste, True)

    def test_jogar_papel_contra_tesoura_para_peder(self):
        jogo = PedraPapelTesoura(EnumPPT.TESOURA)
        teste = jogo.jogo(2)
        self.assertEqual(teste, False)

    def test_jogar_tesoura_contra_tesoura_para_perder(self):
        jogo = PedraPapelTesoura(EnumPPT.TESOURA)
        teste = jogo.jogo(3)
        self.assertEqual(teste, False)
