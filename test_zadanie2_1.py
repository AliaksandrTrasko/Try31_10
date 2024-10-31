from zadanie2_1 import *
import unittest

class main_test(unittest.TestCase):
    
    def test_oblicz_liczbe_elementow(self):
        self.assertTrue(oblicz_liczbe_elementow([2, 5, 2.56, "Ola", "Basia", 3756, -1]) == 7, msg="Blad w funkcji oblicz_liczbe_elementow")
        
    def test_minimum_w_liscie(self):
        self.assertTrue(minimum_w_liscie([2, 5, 2.56, 3756, -1]) == -1, msg="Blad w funkcji minimum_w_liscie")
        
    def test_maksimum_w_liscie(self):
        self.assertTrue(maksimum_w_liscie([2, 5, 2.56, 3756, -1]) == 3756, msg="Blad w funkcji maksimum_w_liscie")
        
    def test_oblicz_srednia(self):
        self.assertTrue(oblicz_srednia([2, 5, 2.56, 3756, -1]) == 752.91, msg="Blad w funkcji oblicz_srednia")
        
    def test_oblicz_srednia_import(self):
        self.assertTrue(oblicz_srednia_import([2, 5, 2.56, 3756, -1]) == 752.91, msg="Blad w funkcji oblicz_srednia_import")

    def test_oblicz_srednia_zakresu(self):
        self.assertTrue(oblicz_srednia_zakresu([2, 5, 2.56, 3756, -1], 1, 3) == 3.78, msg="Blad w funkcji oblicz_srednia_zakresu")
        
    def test_zwroc_ocene(self):
        self.assertTrue(zwroc_ocene([2, 5, 2, 3, 3, 3.5, 5, 3.5]) == 3.5, msg="Blad w funkcji zwroc_ocene")
        
    def test_zwroc_ocene_warunek(self):
        self.assertTrue(zwroc_ocene_warunek([2, 5, 2, 3, 3, 3.5, 5, 3.5]) == 3.5, msg="Blad w funkcji zwroc_ocene_warunek")
        
    def test_oblicz_srednia_wazona(self):
        self.assertTrue(oblicz_srednia_wazona([[4, 5], [1, 2], [2, 3.5]]) == 4.14, msg="Blad w funkcji oblicz_srednia_wazona")
        
    def test_zwroc_ocene_ze_sredniej(self):
        self.assertTrue(zwroc_ocene_ze_sredniej(3.75) == 4, msg="Blad w funkcji zwroc_ocene_ze_sredniej")
        
    def test_zwroc_ocene_z_skomplikowanych_warunkow_zaliczenia(self):
        self.assertTrue(zwroc_ocene_z_skomplikowanych_warunkow_zaliczenia([0.5, True, 4.5, False, [2, 3.5, 5, 5]]) == 4.5, msg="Blad w funkcji zwroc_ocene_z_skomplikowanych_warunkow_zaliczenia")
        
    def test_oblicz_liczbe_elementow_2(self):
        self.assertTrue(oblicz_liczbe_elementow([2, 5, 2.56, "Ola", "Basia", 3756, 3, [1, 4], "cokolwiek", 34, 3.14]) == 11, msg="Blad w funkcji oblicz_liczbe_elementow")
        
    def test_minimum_w_liscie_2(self):
        self.assertTrue(minimum_w_liscie([2, 5, 2.56, 3756, -0.23]) == -0.23, msg="Blad w funkcji minimum_w_liscie")
        
    def test_maksimum_w_liscie_2(self):
        self.assertTrue(maksimum_w_liscie([2, 3.123546778, 3.12354677, -1]) == 3.123546778, msg="Blad w funkcji maksimum_w_liscie")
        
    def test_oblicz_srednia_2(self):
        self.assertTrue(oblicz_srednia([0.346, 0, 2.56, 0.348, 1.233]) == 0.9, msg="Blad w funkcji oblicz_srednia")
        
    def test_oblicz_srednia_import_2(self):
        self.assertTrue(oblicz_srednia_import([0.346, 0, 2.56, 0.348, 1.233]) == 0.9, msg="Blad w funkcji oblicz_srednia_import")
        
    def test_oblicz_srednia_zakresu_2(self):
        self.assertTrue(oblicz_srednia_zakresu([0.346, 0, 2.56, 0.348, 1.233], 0, 1) == 0.35, msg="Blad w funkcji oblicz_srednia_zakresu")
        
    def test_zwroc_ocene_2(self):
        self.assertTrue(zwroc_ocene([2, 5, 5, 5, 5, 3.5, 5, 3.5]) == 4.5, msg="Blad w funkcji zwroc_ocene")
        
    def test_zwroc_ocene_warunek_2(self):
        self.assertTrue(zwroc_ocene_warunek([2, 2, 2, 2, 5, 5, 5]) == 2, msg="Blad w funkcji zwroc_ocene_warunek")
        
    def test_oblicz_srednia_wazona_2(self):
        self.assertTrue(oblicz_srednia_wazona([[0.1, 2], [0.5, 3], [0.4, 3.5]]) == 3.1, msg="Blad w funkcji oblicz_srednia_wazona")
        
    def test_zwroc_ocene_ze_sredniej_2(self):
        self.assertTrue(zwroc_ocene_ze_sredniej(4.75) == 5, msg="Blad w funkcji zwroc_ocene_ze_sredniej")
        
    def test_zwroc_ocene_z_skomplikowanych_warunkow_zaliczenia_2(self):
        self.assertTrue(zwroc_ocene_z_skomplikowanych_warunkow_zaliczenia([0.5, True, 5, False, [4, 5, 5, 5]]) == 5, msg="Blad w funkcji zwroc_ocene_z_skomplikowanych_warunkow_zaliczenia")
        


if __name__ == '__main__':
    unittest.main()