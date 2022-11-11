import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self) -> None:
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_alkurahat_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisia_nolla_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaita_nolla_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisosto_kasvattaa_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_kateisosto_vaihtorahat_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_edullinen_kateisosto_rahat_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_kateisosto_kasvattaa_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_kateisosto_vaihtorahat_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)

    def test_maukas_kateisosto_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_kortilla_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_edullinen_kortin_saldo_ei_riita(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

    def test_edullinen_korttiosto_toimii(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")

    def test_maukas_kortilla_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_maukas_kortin_saldo_ei_riita(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

    def test_maukas_korttiosto_toimii(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

    def test_kortin_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortin_lataus_ei_toimi_varastamalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)