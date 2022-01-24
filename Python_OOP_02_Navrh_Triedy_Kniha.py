# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:36:22 2022

@author: Administrator
"""

class Kniha:
    ISBN = str() # ""
    nazov = str()
    autor = str()
    pocet_stran = int() # 0
    zaner = list() # []
    
    def vypis_info(self):
        print("ISBN -->", self.ISBN)
        print("Nazov -->", self.nazov)
        print("Pocet stran -->", self.pocet_stran)

kniha_kreativita_01 = Kniha()
kniha_kreativita_01.nazov = "Uvod do kreativity"
kniha_kreativita_01.pocet_stran = 326

kniha_kreativita_01.vypis_info()

print(dir(Kniha))

kniha_kreativita_01.qr = True
kniha_kreativita_01.stav_dostupnosti = True
print(dir(kniha_kreativita_01))
