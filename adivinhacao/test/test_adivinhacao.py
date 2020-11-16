from unittest import TestCase
from adivinhacao.adivinhacao_error import PerdeuMaiorError, PerdeuMenorError

from adivinhacao.adivinhacao import Advinhacao


class TestAdivinhacao(TestCase):

    def setUp(self):
        self.advinhacao = Advinhacao(1, 1)

    def test_adivinhar_numero_um_com_erro_menor(self):
        with self.assertRaises(PerdeuMenorError):
            self.advinhacao.jogo(2)

    def test_adivinhar_numero_um_com_erro_maior(self):
        with self.assertRaises(PerdeuMaiorError):
            self.advinhacao.jogo(0)

    def test_adivinhar_numero_um_com_acerto(self):
        valor_esperado = True
        self.assertEqual(valor_esperado, self.advinhacao.jogo(1))

    def test_numero_de_igual_a_um(self):
        valor_esperado = 1
        self.assertEqual(valor_esperado, self.advinhacao.numero_de)

    def test_numero_ate_a_um(self):
        valor_esperado = 1
        self.assertEqual(valor_esperado, self.advinhacao.numero_ate)
