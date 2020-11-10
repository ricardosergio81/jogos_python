from unittest import TestCase

from forca.forca import Forca


class TestAdivinhacao(TestCase):

    def setUp(self):
        self.forca = Forca(1)

    def test_palavra_oculta(self):
        pass