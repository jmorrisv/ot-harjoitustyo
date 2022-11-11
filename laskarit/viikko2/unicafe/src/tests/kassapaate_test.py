import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def test_alkutilanne_oikein(self):
        self.assertEqual(self.kassassa_rahaa, 100000)
        self.assertEqual(self.edulliset, 0)
        self.assertEqual(self.maukkaat, 0)


        