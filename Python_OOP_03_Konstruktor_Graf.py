# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 12:31:42 2022

@author: Administrator
"""

class Graf:
    meno = ""
    kategoria = ""
    # Konstruktor
    # Specialna metoda
    def __init__(self, meno="Analyza predaja", kategoria="Kolacovy"):
        self.meno = meno
        self.kategoria = kategoria
        
    def nastav_sirka(self, sirka = 1):
        """Sirka v metroch napr. 5 m"""
        print("Sirka grafu -->", sirka)
        
    def nastav_rozmery(self, sirka = 1, vyska = 3):
        """Sirka v metroch napr. 5 m"""
        print("Sirka grafu -->", sirka)
        print("Vyska grafu -->", vyska)


novy_graf = Graf("Analyza volby do parlamentu 2052", "Kolacove")
novy_graf2 = Graf("Analyza akcnych filmov 2022", "Stlpcove")

novy_graf.nastav_sirka(5)
novy_graf.nastav_sirka()

novy_graf.nastav_rozmery()
novy_graf.nastav_rozmery(6,9)

del novy_graf
del novy_graf2



# print(Graf)
# print(type(Graf))

# # Objekt (instancie triedy)
# # Anonymny objekt
# print("\nAnonymny objekt")
# Graf()
# print(Graf())

# # Konkretny objekt
# print("\nKonkretny objekt")
# graf_kolacovy = Graf()
# print(graf_kolacovy)

# print(Graf() == graf_kolacovy)
# print("Anonymny objekt ID --> ", id(Graf()))
# print("Konkretny objekt ID --> ", id(graf_kolacovy))

# graf_stlpcovy = Graf()
# print(graf_stlpcovy == graf_kolacovy)
# print("\nKonkretny objekt ID --> ", id(graf_stlpcovy))
# print("Konkretny objekt ID --> ", id(graf_kolacovy))

